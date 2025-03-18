"""
Module for initializing OpenAI API client.

This module retrieves the API key and initializes the API client.

Functions:
        - initialize_openai_client: Ret
---------
- `initialize_openai_client(model_name: str, strict: bool = False) -> openai.OpenAI | None:`
"""

from openai import OpenAI
from ctf_assets.utils.helpers import fetch_openai_key

# TODO: create a shared_client instance. 
# Change module so that it creates a single client instance that can be passed around


def initialize_openai_client(strict: bool = True) -> (OpenAI | None):
    """
    Initializes a OpenAI client

    This function attempts to retrieve the OpenAI API key from the system's
    environment variables. If the API key is not found, it either raises a
    RuntimeError (if strict mode is enabled) or issues a warning and returns
    None.

    Args
    -----
        strict (bool, optional): 
            Whether to enforce strict mode. If True (default), raises a RuntimeError, otherwise issues a warning and returns None.

    Returns
    --------
        An OpenAI client instance if the API key is found, otherwise None.
    """


    # Fetch the OpenAI API key
    OPENAI_API_KEY = fetch_openai_key(strict=strict)

    
    if not OPENAI_API_KEY:
        return None
    
    return OpenAI(api_key = OPENAI_API_KEY)