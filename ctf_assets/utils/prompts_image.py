def generate_dalle_prompt(
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
        response_format (str): Format of the response, either "json" (image URLs) or "base64" (encoded images). Defaults to "json".
        language (str): Language for any text appearing in the images. Defaults to "es-PR".

    Returns:
        str: A detailed prompt ready to be passed to DALLE-2 or DALLE-3.
    """

    # GPT-4o-mini system instructions to generate a highly detailed prompt
    gpt_prompt = f"""
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
    Camera shot: Wide-angle panoramic, capturing both the university’s historical elements and its futuristic enhancements.
    Lighting: Bright and natural, mixed with soft neon glows from AI interfaces."

    Now, generate a similar prompt based on the provided theme and tone.
    """

    # Call GPT-4o-mini to generate the detailed prompt
    response = client.responses.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": gpt_prompt}]
    )

    # Extract generated prompt from GPT-4o-mini's response
    detailed_prompt = response["choices"][0]["message"]["content"]

    # Define response format instruction
    if response_format.lower() == "base64":
        format_instruction = "Return the images in JSON format as base64-encoded data: { 'images': ['base64_1', 'base64_2', ...] }."
    else:
        format_instruction = "Return the image URLs in JSON format: { 'images': ['url1', 'url2', ...] }."

    # Final combined prompt for DALLE
    dalle_prompt = (
        f"{detailed_prompt} "
        f"Ensure the composition, details, and background contribute to the story. "
        f"{format_instruction}"
    )

    return dalle_prompt
