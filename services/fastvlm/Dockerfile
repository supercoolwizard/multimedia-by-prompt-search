FROM python:3.10

WORKDIR /app

RUN git clone https://github.com/apple/ml-fastvlm.git

WORKDIR /app/ml-fastvlm

RUN pip install --upgrade pip
RUN pip install -e .
RUN pip install fastapi uvicorn

COPY server.py .

VOLUME ["/models"]

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]
