
def generate_images():
    # TODO: Implement image generation
    return NotImplementedError("Image generation is not yet implemented.")

# from openai import OpenAI
# from ctf_assets.utils.helpers import validate_openai_model
# from ctf_assets.utils.initialize_client import initialize_openai_client
# from ctf_assets.utils.prompts import image_prompt, system_prompt

# model = validate_openai_model("gpt-4o-mini")
# client = initialize_openai_client()

# def generate_images(
#     theme: str = "",
#     tone: str = "neutral",
#     language: str = "es-PR"
#     Response_format: str = "json"
# ) -> str:
#     """
#     Uses GPT-4o-mini to generate a prompt for DALLE-2/DALLE-3 based on 
#     a theme and tone.

#     Args:
#         theme (str): General theme for the image (e.g., "cybersecurity hacker", "futuristic University").
#         tone (str): Mood or atmosphere of the image (e.g., "dark and mysterious", "cheerful"). Defaults to "neutral".
#         language (str): Language for any text appearing in the images. Defaults to "es-PR".
#         Response_format (str): Format of the response, either "json" (image URLs) or "base64" (encoded images). Defaults to "json".

#     Returns:
#         str: A detailed prompt ready to be passed to DALLE-2 or DALLE-3.
#     """

#     # GPT-4o-mini system instructions to generate a highly detailed prompt
#     input = image_prompt(
#         theme=theme,
#         tone=tone,
#         language=language
#     )
  
#     # Call GPT-4o-mini to generate the detailed prompt
#     response = client.responses.create(
#         model="gpt-4o-mini",
#         instructions=system_prompt(),
#         input= input,
#     )

#     # Extract generated prompt from GPT-4o-mini's response
#     detailed_prompt = response.output_text

#     detailed_prompt = (
#         f"{detailed_prompt} "
#         f"Ensure the composition, details, and background contribute to the story. "
#         f"{format_instruction}"
#     )

#     # Image generation with DALLE
#     image_generation_response = client.images.generate(
#         model="dall-e-3",
#         prompt= detailed_prompt,
#         size="1024x1024",
#         style= "natural"
#         quality="hd",
#         n=1,
#     )

#     image = print(response.images[0].url  # TODO: Need to implement url or binary image data
# )
    
#     return image