# Part of this code is from OpenAI code from openai website

from openai import OpenAI
from ctf_assets.config import fetch_openai_key

key = fetch_openai_key(strict=True)

client = OpenAI()

img = client.images.generate(
  model="dall-e-3",
  prompt="A cute baby sea otter",
  n=1,
  response_format="b64_json",
  size="1024x1024"
)

print(img)