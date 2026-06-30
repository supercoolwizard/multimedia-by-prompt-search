# multimedia-by-prompt-search

A local, prompt-driven search engine for your image and video libraries.
Describe what you're looking for in plain English, and the system surfaces
the matching files (and, for videos, the matching frames) from a folder on
your machine.

The pipeline is offline-friendly: a vision-language model captions your
media, a sentence encoder embeds those captions, and a local Qdrant vector
DB handles similarity search.

---

## How it works

There are two stages.

**1. Indexing — `main_encoder.py`**

Walks a directory, detects media type per file, and builds a searchable index:

- **Images**: opened with PIL, captioned by `FastVLM-1.5B`.
- **Videos**: sliced into timestamps, frames are extracted with `ffmpeg`,
  and each frame is captioned by `FastVLM-1.5B`.

Each caption is embedded with `BAAI/bge-small-en-v1.5` (384-dim) and stored,
together with file path, description and (for frames) timestamp, in a
local Qdrant collection.

**2. Searching — `main_decoder.py`**

A small CLI that:

1. Takes a natural-language prompt.
2. Embeds it with the same BGE encoder.
3. Queries Qdrant for the top matches.
4. Prints a Rich table with the path, similarity score, and caption.
5. Reveals the selected file in Finder/Explorer.

---

## Project layout

```
domain/            Domain entities (Multimedia dataclass)
application/       Use cases, ports, and service strategies
  ports/           Interface contracts (TextEncoder, ImageDescriber, VectorDatabase, ...)
  services/        ImageProcessor, VideoProcessor, MultimediaDispatcher
infrastructure/    Concrete adapters
  bge_small_encoder.py
  fastvlm_image_describer.py
  qdrant/          Local Qdrant client + output processor
  services/        Video slicer, ffmpeg bridge, type detector, id generator
cli/               CLI decoder, Rich table, platform file revealer
tests/             Unit + integration tests
experiments/       Notebooks and ad-hoc inspection scripts
```

The codebase follows a hexagonal / ports-and-adapters layout: the
`application/` layer defines interfaces (`ports/`), and `infrastructure/`
provides the concrete implementations (BGE, FastVLM, Qdrant, ffmpeg).

---

## Requirements

- Python 3.12+
- [`ffmpeg`](https://ffmpeg.org/) available on `PATH` (used to extract video frames)
- A Hugging Face token with access to `apple/FastVLM-1.5B`
- macOS, Linux, or Windows (the file reveal step is platform-aware)

Dependencies are installed into the local `.venv` in this repo.

---

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -U pip
pip install requirements.txt
```

Models are downloaded on first run by `transformers`.

Create a `config.env` file in the project root:

```
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxx
```

---

## Configuration

Edit `settings.py`:

```python
TARGET_DIR   = Path("testing")   # folder the encoder will index
SEARCH_SCOPE = 2                 # how many results the decoder returns
```

Anything you drop into `TARGET_DIR` (or change it to point anywhere on
disk) will be indexed the next time you run the encoder.

---

## Usage

**Index your media**

```bash
python main_encoder.py
```

The encoder will iterate every file in `TARGET_DIR`, skip anything that
isn't an image or video, and write vectors to `data/qdrant/`.

**Search**

```bash
python main_decoder.py "a cat sitting on a windowsill at sunset"
```

You will see a table like:

```
Index | Best Match Path         | Score | Description
------|-------------------------|-------|------------------------------------
0     | testing/cats/frame.jpg  | 0.91  | An orange cat on a windowsill...
1     | testing/videos/sun.mp4  | 0.84  | frame at 00:01:23 ...
```

Pick an index and the file is opened in your OS file manager at the
matching location.

---

## Models

| Role                | Model                       | Notes                                |
|---------------------|-----------------------------|--------------------------------------|
| Image captioning    | `apple/FastVLM-1.5B`        | Vision-language model from Apple     |
| Text embeddings     | `BAAI/bge-small-en-v1.5`    | 384-dim, English                     |
| Vector DB           | Qdrant (local on-disk mode) | Cosine similarity, collection `multimedia` |

Swap any of these by writing a new adapter that implements the relevant
port in `application/ports/` and wiring it up in `main_*.py`.

---

## Tests

```bash
source .venv/bin/activate
pytest tests/
```

- `tests/unit/` — pure-logic tests (image processor, etc.)
- `tests/integration/` — tests against the real BGE / FastVLM / Qdrant adapters

---

## Notes

- The first run downloads the BGE and FastVLM weights; make sure your
  HF token has access to `apple/FastVLM-1.5B`.
- Video indexing is slower because each selected timestamp triggers a
  FastVLM captioning pass.
- `data/` (Qdrant storage) and `config.env` are git-ignored — re-indexing
  is required after a clean clone.

---

## Experiments

Proposed solution was tested against SOTA CLIP architecture with the following results:

```
===== Retrieval Summary =====
Hit@1: 17/30 (56.7%)
Hit@2: 20/30 (66.7%)
Hit@3: 22/30 (73.3%)
Hit@4: 27/30 (90.0%)
MRR: 0.6806
```

![my solution](/assets/mine.png)
(closer to identity matrix – better)

vs

```
===== CLIP Retrieval Summary ===== 
Hit@1: 15/30 (50.0%) 
Hit@2: 18/30 (60.0%) 
Hit@3: 19/30 (63.3%) 
Hit@4: 19/30 (63.3%) 
MRR: 0.5611
```

![clip](/assets/clip.png)
(closer to identity matrix – better)

> [!IMPORTANT]
> If the prompt is less detailed, CLIP architecture will inevitably win, but when prompt is detailed – proposed solution will perform better.

