from services.fastvlm_image_describer import FastVLMImageDescriber

image = "images/1.jpg"

client = FastVLMImageDescriber()
client.describe(image)
