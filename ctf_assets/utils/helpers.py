"""
Helper functions for environment management and model validation.

This module provides:
- Loading of environment variables and retrieval of API keys 
- Model availability.

Functions:
----------
- `fetch_openai_key(strict: bool = True) -> str | None:`
- `validate_openai_model(model_name: str) -> str:`
"""

import os
import warnings
from openai import OpenAI
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file if it exists
dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path=dotenv_path)

def fetch_openai_key(strict: bool = True) -> str | None:
    """
    Fetches the OpenAI API key from the environment.

    This function looks for the API key in the system environment variables or 
    in the `.env` file of the project. If it does not find the API key or it is
    an empty string, it raises a RuntimeError if strict=True, otherwise it 
    logs a warning and returns None.

    Args:
        strict (bool): Controls what happens if API key is missing. Defaults to True.
            - If `strict=True`, raises a RuntimeError.
            - If `strict=False`, logs a warning and returns None.

    Returns:
        (str | None): The API key if found, otherwise None.

    Raises:
        RuntimeError: If `strict=True` and the key is missing.
    """
    key = os.getenv("OPENAI_API_KEY") 

    if not key: 
        message = (
            f"OPENAI_API_KEY is missing! "
            "Set it in your system environment variables or .env file."
        )
        if strict:
            raise RuntimeError(message) 
        warnings.warn(f"{message} Returning None.")  
        return None  
    
    return key

def validate_openai_model(model_name: str) -> str:
    '''
    Check if the provided model is currently supported.

    Args:
        model_name (str): The model passed by the user.
    
    Returns
        (str): The model name if it is supported, otherwise
        "gpt-4o-mini".
    '''
    # TODO: implement caching so that it only creates the supported models once per session
    
    # Initialize a OpenAI API client
    client = OpenAI()
    
    # Retrieve list of currently supported OpenAI API models
    supported_models = [model.id for model in client.models.list()]
    
    model_name = model_name.lower()  # Normalize model name
    
    return model_name if model_name in supported_models else "gpt-4o-mini"