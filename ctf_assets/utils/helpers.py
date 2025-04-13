"""
Helper functions for environment management and model validation.

This module provides:
- Loading of environment variables and retrieval of API keys 
- Model availability.

Functions:
----------
- `fetch_openai_key(strict: bool = True) -> str | None:`
- `validate_openai_model(model: str) -> str:`
"""

# import os
# import warnings
from openai import OpenAI
from ctf_assets.config import fetch_openai_key

# Cache OpenAI currently supported models and reasoning models, initially set to None
supported_openai_models = None
reasoning_openai_models = None
image_models = None

# # Load environment
# load_dotenv()

# def fetch_openai_key(strict: bool = True) -> str | None:
#     """
#     Fetch the OpenAI API key from the environment variables.

#     This function looks for the OpenAI API key in the system environment variables 
#     or in the `.env` file. If the key is found, it returns the key as a string. 
#     If the key is not found, it raises an exception or logs a warning based on 
#     the `strict` parameter.

#     Args:
#         strict (bool): Determines the behavior if the API key is missing.
#             - If `strict=True`, a `RuntimeError` is raised.
#             - If `strict=False`, a warning is logged, and `None` is returned.
#             Defaults to `True`.

#     Returns:
#         str | None: The OpenAI API key if found, otherwise `None` if `strict=False`.

#     Raises:
#         RuntimeError: If `strict=True` and the API key is missing.

#     Example:
#         >>> fetch_openai_key()
#         'your-openai-api-key'

#         >>> fetch_openai_key(strict=False)
#         None
#     """
#     key = os.getenv("OPENAI_API_KEY")

#     if not key:
#         message = (
#             f"OPENAI_API_KEY is missing! "
#             "Set it in your system environment variables or .env file."
#         )
#         if strict:
#             raise RuntimeError(message)
#         warnings.warn(f"{message} Returning None.")
#         return None

#     return key

def get_supported_openai_models():
    """
    Retrieve and cache the list of all supported OpenAI models.

    This function retrieves the list of currently supported OpenAI models from 
    the OpenAI API and caches them for future use. If the list of supported 
    models has already been cached, the function will return the cached list 
    without making another API call.

    Returns:
        list: A list of supported OpenAI model IDs.

    Example:
        >>> get_supported_openai_models()
        ["gpt-3.5-turbo", "gpt-4", "text-davinci-003"]
    """
    global supported_openai_models

    if supported_openai_models is None:
        # Initialize an OpenAI API client
        client = OpenAI(api_key=fetch_openai_key(strict=True))

        # Retrieve list of currently supported OpenAI API models
        supported_openai_models = [model.id for model in client.models.list()]

    return supported_openai_models

def get_reasoning_openai_models():
    """
    Retrieve and cache the list of OpenAI reasoning models.

    This function retrieves the list of all supported OpenAI models using 
    the `get_supported_openai_models()` function and filters them to include 
    only the reasoning models, which are defined as models whose IDs start 
    with the character "o". The reasoning models are then cached for future use.

    If the reasoning models have already been cached, the function will return 
    the cached list without making an API call.

    Returns:
        list: A list of supported OpenAI reasoning model IDs.

    Example:
        >>> get_reasoning_openai_models()
        ["o-model1", "o-model2", "o-model3"]
    """
    global reasoning_openai_models

    if reasoning_openai_models is None:
        # Initialize an OpenAI API client
        client = OpenAI(api_key=fetch_openai_key(strict=True))

        # Retrieve list of currently supported OpenAI models
        supported_openai_models = get_supported_openai_models()

        # Filter the models to include reasoning models (those that start with "o")
        reasoning_openai_models = [model for model in supported_openai_models if model.startswith("o")]

    return reasoning_openai_models
 
def validate_openai_model(model: str) -> str:
    """
    Check if the provided OpenAI model is currently supported.

    This function checks if the given model name is present in the list of 
    supported OpenAI models. If the model is supported, it returns the 
    model name. If the model is not supported, it returns a default model 
    name, "gpt-4o-mini".

    Args:
        mode (str): The name of the OpenAI model to validate.

    Returns:
        str: The provided model name if it is supported, otherwise 
             "gpt-4o-mini".
    
    Example:
    validate_openai_model("gpt-4")
    "gpt-4"
    
    validate_openai_model("invalid-model")
    "gpt-4o-mini"
    """
    global supported_openai_models
    
    if supported_openai_models is None:
        # Retrieve list of currently supported OpenAI API models
        supported_openai_models = get_supported_openai_models()

    return model if model in supported_openai_models else "gpt-4o-mini"

def get_image_models():
    """
    Retrieve and cache the list of OpenAI image models.
    This function retrieves the list of all supported OpenAI models using
    the `get_supported_openai_models()` function and filters them to include
    only the image models, which are defined as models whose IDs start with the characters "dall".
    The image models are then cached for future use.
    If the image models have already been cached, the function will return
    the cached list without making an API call.
    Returns:
        list: A list of supported OpenAI image model IDs.
    Example:
        >>> get_image_models()
        ["dall-e-2", "dall-e-3"]
    """
    global supported_openai_models
    global image_models

    if image_models is None:
        # Initialize an OpenAI API client
        client = OpenAI(api_key=fetch_openai_key(strict=True))

        # Retrieve list of currently supported OpenAI models
        supported_openai_models = get_supported_openai_models()

        # Filter the models to include image models (those that start with "dall")
        image_models = [model for model in supported_openai_models if model.startswith("dall")]
    
    return image_models