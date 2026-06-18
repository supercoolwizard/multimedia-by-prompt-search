from infrastructure.clients.fastvlm_client import FastVLMClient

image = "images/1.jpg"

client = FastVLMClient()
client.describe(image)
