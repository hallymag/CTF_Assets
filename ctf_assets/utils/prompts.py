"""
Module for generating structured prompts for Capture the Flag (CTF) challenges.

This module creates structured prompts to guide the LLM content generation. It
has prompts for generating: flags, stories, and images. The prompts are designed
to guide generation while ensuring adherence to security and ethical guidelines.

Functions:
    - system_prompt: Constructs a structured prompt for system level constraints.
    - flag_prompt: Constructs a structured prompt for flag generation.
    - story_prompt: Constructs a structured prompt for story generation.
    - image_prompt: Constructs a structured prompt for image generation.

Usage:
    from openai import openai
    from prompts import system_prompt, flag_prompt
    
    system_content = system_prompt("Ensure all content is beginner-friendly.")
    flag_content = flag_prompt(theme="Space Exploration", tone="funny", amt=3, language="en")

Notes: 
    In newer models, the system_prompt is not necessary. The models are
    trained to avoid generating illegal or inappropriate content. However,
    it is still useful in order to provide additional guidelines or 
    constraints for the model to follow.
"""

def system_prompt(additional_system_instructions: str = "") -> str:
    """
    Generates a system-level prompt that ensures content is legal, appropriate 
    for high school students under 18, and follows cybersecurity CTF guidelines.

    Args:
        additional_system_instructions (str): Extra system constraints. Defaults to "".

    Returns:
        str: A detailed system-level prompt.
    """
    prompt = (
        "You are an expert cybersecurity assistant. "
        "You must ensure all content is legal and appropriate for high school students under 18. "
        "You generate content for Capture the Flag (CTF) challenges. "
        f"{additional_system_instructions}"
    )
    return prompt


def flag_prompt(
    theme: str = "",
    tone: str = "neutral",
    amt: int = 1,
    flag_format: str = "ctf{..}",
    language: str = "es-PR",
    additional_instructions: str = "",
    additional_system_instructions: str = ""
) -> str:
    """
        Generates a prompt that ensures flags follow the given theme, tone, and format while enforcing 
        system-level instructions.
        
        Args:
            theme (str): Theme of the flags. Defaults to "".
            tone (str): Tone of the flags (e.g., "serious", "playful"). Defaults to "neutral".
            amt (int): Number of flags to generate (must be ≥ 1). Defaults to 1.
            flag_format (str): Format of the flags (e.g., "ctf{...}"). Defaults to "ctf{..}".
            language (str): Language of the flags. Defaults to "es-PR".
            additional_instructions (str): Extra constraints for flag generation. Defaults to "".
            additional_system_instructions (str): System-level constraints. Defaults to "".

        Returns:
            str: A detailed prompt designed to guide the LLM when generating flags.
        """
    amt = max(1, amt)
    sys_prompt = system_prompt(additional_system_instructions)

    prompt = (
        f"{sys_prompt} "
        f"Generate exactly {amt} unique CTF flags in {language}, based on the theme: '{theme}'. "
        f"If a tone is specified, apply: '{tone}'. "
        f"Each flag must strictly follow this format: '{flag_format}'. "
        f"All flags must be distinct, logically structured, and thematically relevant. "
        f"\n\nIMPORTANT: You must generate exactly {amt} flags—no more, no less. \n\n"
        f"The response must be in the following valid JSON format, with no additional text:\n\n"
        f'{{"flags": ["flag_1", "flag_2", ..., "flag_{amt}"]}}\n\n'
        f"Do not include explanations, preambles, or any text outside the JSON response. "
        f"If the number of flags is incorrect or the format is not followed, the output is invalid. "
        f"{additional_instructions}"
    )

    return prompt

def story_prompt(
    theme: str = "",
    tone: str = "neutral",
    amt: int = 1,
    language: str = "es-PR",
    additional_instructions: str = "",
    additional_system_instructions: str = ""
) -> str:
    """
    Generates a prompt that ensures stories follow the given theme and tone 
    while enforcing system-level instructions. Titles are excluded.

    Args:
        theme (str): Theme of the stories. Defaults to "".
        tone (str): Tone of the stories (e.g., "mysterious", "cheerful"). Defaults to "neutral".
        amt (int): Number of stories to generate (must be ≥ 1). Defaults to 1.
        language (str): Language of the stories. Defaults to "es-PR".
        additional_instructions (str): Extra constraints for story generation. Defaults to "".
        additional_system_instructions (str): System-level constraints. Defaults to "".

    Returns:
        str:  A detailed prompt to guide the LLM when generating stories.
    """
    amt = max(1, amt)
    sys_prompt = system_prompt(additional_system_instructions)

    prompt = (
        f"{sys_prompt} "
        f"Generate exactly {amt} unique stories in {language} based on the theme: '{theme}'. "
        f"If a tone is specified, use: '{tone}'. "
        f"Each story must have a unique plot, characters, and setting. "
        f"Do NOT include titles in any of the stories. "
        f"You must generate exactly {amt} stories—no more, no less. "
        f"Respond in valid JSON format with an array of stories, structured as follows: \n\n"
        '{{"stories": [{{"story": "Story content..."}}, {{"story": "Another story content..."}}, ..., {{"story{amt}": "Final story content..."}}]}} \n\n'
        "Do not include explanations, preambles, or any text outside the JSON response. "
        f"If you do not generate exactly {amt} stories, the output is incorrect. "
        f"{additional_instructions}"
    )
    
    return prompt

def story_prompt_with_title(
    theme: str = "",
    tone: str = "neutral",
    amt: int = 1,
    language: str = "es-PR",
    additional_instructions: str = "",
    additional_system_instructions: str = "",
) -> str:
    """
    Generates a prompt that ensures stories follow the given theme and tone while enforcing 
    system-level instructions. Titles are included.

    Args:
        theme (str): Theme of the stories. Defaults to "".
        tone (str): Tone of the stories (e.g., "mysterious", "cheerful"). Defaults to "neutral".
        amt (int): Number of stories to generate (must be ≥ 1). Defaults to 1.
        language (str): Language of the stories. Defaults to "es-PR".
        additional_instructions (str): Extra constraints for story generation. Defaults to "".
        additional_system_instructions (str): System-level constraints. Defaults to "".

    Returns:
        str:  A detailed prompt to guide the LLM when generating stories with titles.
    """
    amt = max(1, int(amt))
    sys_prompt = system_prompt(additional_system_instructions)

    prompt = (
        f"{sys_prompt} "
        f"Generate exactly {amt} unique stories in {language} based on the theme: '{theme}'. "
        f"If a tone is specified, use: '{tone}'. "
        f"Each story must have a unique plot, characters, and setting, and must include a title. "
        f"You must generate exactly {amt} stories—no more, no less. "
        f"Respond in valid JSON format with an array of stories, structured as follows:\n\n"
        f'{{"stories": [{{"title": "Story Title 1", "story": "Story content..."}}, '
        f'{{"title": "Story Title 2", "story": "Another story content..."}}, ..., '
        f'{{"title": "Story Title {amt}", "story": "Final story content..."}}]}}\n\n'
        f"Do not include explanations, preambles, or any text outside the JSON response. "
        f"If you do not generate exactly {amt} stories, the output is incorrect. "
        f"{additional_instructions}"
    )

    return prompt

def image_prompt(
    theme: str,
    tone: str = "neutral",
    response_format: str = "json",
    language: str = "es-PR"
) -> str:
    """
    Uses GPT-4o-mini to generate a prompt for DALLE-2/DALLE-3 based on 
    a theme and tone.

    Args:
        theme (str): General theme for the image (e.g., "cybersecurity hacker", "futuristic University").
        tone (str): Mood or atmosphere of the image (e.g., "dark and mysterious", "cheerful"). Defaults to "neutral".
        language (str): Language for any text appearing in the images. Defaults to "es-PR".

    Returns:
        str: A detailed prompt ready to be passed to DALLE-2 or DALLE-3.
    """

    # GPT-4o-mini system instructions to generate a highly detailed prompt
    prompt = f"""
    You are an AI assistant that generates structured prompts for AI image generation.
    Your task is to take a given theme and tone and create a highly detailed and visually descriptive 
    prompt optimized for DALLE-2 and DALLE-3. 

    The generated prompt must include:
    - A vivid **scene description** that sets the stage for the image.
    - **Key visual elements** that make the image stand out.
    - **Lighting and atmosphere** to enhance realism.
    - **Depth and camera perspective** (e.g., "wide-angle shot", "close-up", "over-the-shoulder").
    - A **composition style** that aligns with the theme and tone.

    The theme is: **"{theme}"**
    The mood and tone should be: **"{tone}"**
    The image must contain fine details, accurate lighting, and a cinematic composition.
    If the image includes text, ensure it is in **{language}**.

    ### Example 1: Cybersecurity Hacker
    "A dimly lit cyberpunk cityscape, glowing neon signs reflecting off the wet streets. 
    A lone hacker, wearing a high-tech visor, sits at a terminal surrounded by holographic data streams. 
    The atmosphere is dark and mysterious, with backlit silhouettes adding depth. 
    Camera shot: Over-the-shoulder perspective, dramatic contrast between shadows and neon lights."

    ### Example 2: University Campus of the Future
    "A futuristic version of Universidad de Puerto Rico, Recinto de Río Piedras, with students in 
    a next-generation AI-powered computer lab. Transparent holographic screens project real-time code 
    as students engage in collaborative programming exercises. 
    Lush tropical gardens blend with solar-powered smart classrooms. 
    Camera shot: Wide-angle panoramic, capturing both the historical elements of the unviersity and its futuristic enhancements.
    Lighting: Bright and natural, mixed with soft neon glows from AI interfaces."

    Now, generate a similar prompt based on the provided theme and tone.
    """
    
    return prompt
