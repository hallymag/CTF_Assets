import argparse
import importlib    # To import modules at runtime instead of hardcoding them

def main():
    parser = argparse.ArgumentParser(description="CTF Assets Generator CLI")

    # Choose the module for asset generation
    parser.add_argument(
        "module", 
        type=str, 
        choices=["flags", "stories", "images"],
        help= "Module to use to generate assets (e.g. flags, stories, images)"
    )

    # Choose the function to call to generate assets
    parser.add_argument(
        "function",
        type=str,
        help="Function to call to generate assets. One of generate_flags, generate_stories, generate_images"
    )

    # Common parameters that can be used for all modules
    parser.add_argument("--theme", type=str, default= "", help= "Theme for the CTF challenge")
    parser.add_argument("--tone", type=str, default="neutral", help="Tone to use (e.g. neutral, funny, formal)")
    parser.add_argument("--amt", type=int, default=1, help="How many to generate")
    parser.add_argument("--model", type=str, default="gpt-4o-mini", help="OpenAI model to use")
    parser.add_argument("--flag-format", type=str, default="ctf{...}", help="Format of the flag (e.g., ctf{...})")
    parser.add_argument("--response-format", type=str, default="JSON", help="Format of the response (e.g. JSON or [item1, item2, item3])")
    parser.add_argument("--language", type=str, default="es-PR", help="Language for the generated flag")
    parser.add_argument("--additional-instructions", type=str, default="", help="Additional user level constraints")
    parser.add_argument("--additional-system-instructions", type=str, default="", help="Additional system level constraintsins")

    args = parser.parse_args()

    mappings = {
        "flags": "ctf_assets.flag_generator",
        "stories": "ctf_assets.story_generator",
        "images": "ctf_assets.image_generator",
    }

    # retrieve the module name from the mappings dictionary
    module_name = mappings[args.module]

    try:
        # Import the module at runtime
        module = importlib.import_module(module_name)

        # Get the function to call from the module
        func = getattr(module, args.function)

        # Call the function dynamically
        result = func(theme=args.theme, tone=args.tone, amt=args.amt,
                      model=args.model, response_format=args.response, language=args.language,
                      category=args.category, tags=args.tags)

        print(result)

    except ModuleNotFoundError:
        print(f"Error: Module '{module_name}' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()