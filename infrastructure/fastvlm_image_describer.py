from application.ports.image_describer import ImageDescriber
import torch
from PIL import Image
from transformers import AutoTokenizer, AutoModelForCausalLM


class FastVLMImageDescriber(ImageDescriber):
    def __init__(self, hf_token, config):
        self.model_name = "apple/FastVLM-1.5B"
        self.tokenizer = AutoTokenizer.from_pretrained(
            self.model_name, 
            trust_remote_code=True, 
            token=hf_token,
        )
        self.model = AutoModelForCausalLM.from_pretrained(
            self.model_name,
            dtype=config.dtype,
            trust_remote_code=True,
            token=hf_token,
        ).to(config.device)

    def describe(self, image, prompt):
        messages = [
            {"role": "user", "content": f"<image>\n{prompt}"}
        ]

        rendered = self.tokenizer.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
        pre, post = rendered.split("<image>", 1)

        pre_ids  = self.tokenizer(pre,  return_tensors="pt", add_special_tokens=False).input_ids
        post_ids = self.tokenizer(post, return_tensors="pt", add_special_tokens=False).input_ids

        img_tok = torch.tensor([[-200]], dtype=pre_ids.dtype)
        input_ids = torch.cat([pre_ids, img_tok, post_ids], dim=1).to(self.model.device)
        attention_mask = torch.ones_like(input_ids, device=self.model.device)

        px = self.model.get_vision_tower().image_processor(images=image, return_tensors="pt")["pixel_values"]
        px = px.to(self.model.device, dtype=self.model.dtype)

        with torch.inference_mode():
            out = self.model.generate(
                inputs=input_ids,
                attention_mask=attention_mask,
                images=px,
                max_new_tokens=64,
            )
        return self.tokenizer.decode(out[0], skip_special_tokens=True)

