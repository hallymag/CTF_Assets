import os
import openai
from openai import OpenAI 
from ctf_assets.config import fetch_openai_key
from warnings import warn
from ctf_assets.utils.prompts import image_prompt

def image_directory():
    # set a directory to save DALL·E images to
    image_dir_name = "downloaded_images"
    image_dir = os.path.join(os.curdir, image_dir_name)

    # create the directory if it doesn't yet exist
    if not os.path.isdir(image_dir):
        os.mkdir(image_dir)

    # print the directory to save to
    print(f"Image directory: {image_dir}\n")

def generate_images(image_model: str="dall-e-2", 
                    theme: str="", 
                    tone: str="", 
                    amt: int=1, 
                    style: str="vivid", 
                    quality: str="standard", 
                    size: str="1024x1024",
                    prompt_model: str="gpt-40-mini"):

    api_key = fetch_openai_key()

    client = OpenAI(api_key=api_key)
    
    if image_model.lower() not in ["dall-e-2", "dall-e-3"]:
        print(f"Invalid image model: {image_model}. Defaulting to DALL-E 2.")
        warn(f"Invalid image model: {image_model}. Defaulting to DALL-E 2.")
        image_model = "dall-e-2"

    # DALLE-3 can only generate 1 image at a time
    if image_model == "dall-e-3": 
        amt=1
    # DALLE-2 can generate 1-10 images at a time
    else:
        if amt >= 10: 
            amt = 10
        elif amt > 0: 
            amt = int(amt)
        else: 
            amt = 1

    prompt= image_prompt(
        theme=theme,
        tone = tone, 
        amt = amt,
        language = "es-PR")

    print(f"Prompt: {prompt}\n")

    # Generate an image prompt
    try:
        response = client.responses.create(
            model=prompt_model,
            input=prompt,
        )
    except openai.OpenAIError as e:
        print(f"[ERROR] Generating prompt. OpenAI API error: {e}")
        return 1

    # Extract the generated prompt
    prompt_t2i= response.output_text

    try:
        img = client.images.generate(
            image_model="model",
            prompt=prompt_t2i,
            n=amt,
            size=size,
            quality=quality,
            style=style,
            # response_format= "b64_json"
    )
    except openai.OpenAIError as e:
        print(f"[ERROR] Generating images. OpenAI API error: {e}")
        return 1
    print(response.data[0].url)
