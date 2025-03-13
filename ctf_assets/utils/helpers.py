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
    Fetches the OpenAI API key from environment variables.

    This function looks for the OpenAI API key first in the system
    environment, then in the `.env` file of the project. If the key is
    not found, it raises a RuntimeError or issues a warning based on the
    value of `strict`.:
    - If `strict=True`, it raises a RuntimeError.
    - If `strict=False`, it issues a warning and returns None.

    Args
    ----
        strict (bool, optional): Controls whether a missing key raises an
            erro
            If strict=True (default) enforce strict mode.
            If the key is missing from the environment variables, and
            strict=True` (default), it raises a RuntimeError.
            - `strict=False` it logs a warning and returns None.

    Returns
    -------
        str | None: The OpenAI API key if found, otherwise None.

    Raises
    ------
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
    Check if model is currently supported by the OpenAI API.

    Args
    ---
        model_name (str): The openai model passed by the user.
    
    Returns
    -------
        model_name (str): OpenAI model to use.
        Defaults to "gpt-4o-mini" if the provided model is not supported.
    '''
    
    # Initialize a OpenAI API client
    client = OpenAI()
    
    # Retrieve list of currently supported OpenAI API models
    supported_models = [model.id for model in client.models.list()]
    
    return model_name if model_name in supported_models else "gpt-4o-mini"