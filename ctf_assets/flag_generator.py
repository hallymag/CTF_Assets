"""
Flag Generator Module for CTF Challenges.

This module provides functionality to generate Capture The Flag (CTF) flags
using an LLM (Large Language Model) API. It builds a prompt based on user-defined 
parameters such as theme, tone, flag format, and more, and interacts with the 
OpenAI API to generate flags accordingly.

Functions:
    generate_flags: Generates one or more CTF flags based on provided parameters.

Example:
    flags = generate_flags(
        theme="Hackathon",
        tone="neutral",
        amt=3,
        model="gpt-4o-mini",
        flag_format="ctf{..}",
        language="es-PR",
        additional_instructions="Flags must be under 50 characters.",
        additional_system_instructions="You are an assistant that avoids fabricating information.",
        temperature=0.65
    )
    print(flags)
"""

from openai import OpenAIError
from openai import OpenAI
import json
from ctf_assets.utils.helpers import validate_openai_model, get_reasoning_openai_models
from ctf_assets.utils.prompts import flag_prompt
from ctf_assets.schema.json_schema import get_flag_schema
from ctf_assets.config import fetch_openai_key
from ctf_assets.utils.response_parser import parse_flags

def generate_flags(
        theme: str = "",
        tone: str = "neutral",
        amt: int = 1,
        model: str = "gpt-4o-mini",
        flag_format: str = "ctf{..}",
        language: str = "es-PR",
        additional_instructions: str = "",
        additional_system_instructions: str = "",
        temperature: float = 0.65
) -> list[str]:
    """
    Generate CTF flags using an LLM based on the provided parameters.

    This function constructs a prompt tailored to the user's requirements and 
    sends it to the OpenAI API to generate a set of flags. It supports 
    customization of the flag theme, tone, format, language, and additional 
    instructions to fine-tune the generation.

    Args:
        theme (str): The thematic context for the flags. Defaults to an empty string.
        tone (str): Desired tone for the flags (e.g., neutral, playful). Defaults to "neutral".
        amt (int): Number of flags to generate. Must be 1 or higher. Defaults to 1.
        model (str): OpenAI model name to use for generation. Defaults to "gpt-4o-mini".
        flag_format (str): Format template for the flag, e.g., "ctf{..}". Defaults to "ctf{..}".
        language (str): Language code for flag generation. Defaults to "es-PR".
        additional_instructions (str): Optional extra instructions for flag generation. Defaults to an empty string.
        additional_system_instructions (str): Optional system-level instructions for the LLM. Defaults to an empty string.
        temperature (float): Sampling temperature for generation randomness. Defaults to 0.7.

    Returns:
        dict: A dictionary containing the generated flags.

    Raises:
        ValueError: If the OpenAI client fails to initialize.
    """
    
    # Load environment
    
    # Validate model selection. If the model is not supported, default to "gpt-4o-mini"
    model = validate_openai_model(model_name=model) 

    # # Initialize OpenAI API client
    # client = openai.OpenAI()

    # Initialize OpenAI API client
    client = OpenAI(api_key=fetch_openai_key(strict=True))

    if client is None:
        raise ValueError("OpenAI client failed to initialize. Exiting.")

    # Construct the prompt using provided parameters
    prompt = flag_prompt(
        asset_type="flags",
        theme=theme,
        tone=tone,
        amt=max(1, amt),  # Ensure at least one flag is generated
        flag_format=flag_format,
        language=language,
        additional_instructions=additional_instructions,
        additional_system_instructions=additional_system_instructions,
    )

    openai_reasoning_models = get_reasoning_openai_models()

    # Get the flag schema as a dict directly without converting it to a string
    flag_schema = get_flag_schema()

    responses_parameters= {
        "model": model,
        "input": prompt,
        "text": flag_schema,
    }

    if model not in openai_reasoning_models:
        # Add the temperature parameter to the responses_parameters dictionary
        responses_parameters["temperature"] = temperature

    try:
        if model not in openai_reasoning_models:          # Generate flags using Responses from OpenAI
            response = client.responses.create( 
                model=model,
                temperature=temperature,
                input=prompt,
                text=flag_schema
            )
        else:
            # Generate flags using OpenAI Completions
            response = client.responses.create( 
                model=model,
                input=prompt,
                text=flag_schema
            )

    except OpenAIError as e:
        print(f"[ERROR] OpenAI API error: {e}")
        return 1
    
    return parse_flags(response=response.output_text)
