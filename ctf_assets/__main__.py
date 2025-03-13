import argparse
from ctf_assets.flag_generator import generate_flags  # Example import

def main():
    parser = argparse.ArgumentParser(description="CTF Assets Generator CLI")

    parser.add_argument("--theme", type=str, default= "", help= "Theme for the CTF challenge")
    parser.add_argument("--tone", type=str, default="neutral", help="Tone of the flag")
    parser.add_argument("--amt", type=int, default=1, help="Number of flags to generate")
    parser.add_argument("--model", type=str, default="gpt-4o-mini", help="LLM model to use")
    parser.add_argument("--flag", type=str, default="ctf{This is a flag}", help="Format of the flag (e.g., ctf{})")
    parser.add_argument("--response", type=str, default="JSON", help="Format of the response (e.g., JSON, list)")
    parser.add_argument("--language", type=str, default="es-PR", help="Language for the generated flag")
    parser.add_argument("--category", type=str, default="", help="Challenge category (optional)")
    parser.add_argument("--tags", type=str, default="", help="Tags for the challenge (optional)")
    parser.add_argument("--additional-flag-instructions", type=str, dest="additional_flag_instructions", default="", help="Additional flag instructions")
    parser.add_argument("--additional-system-instructions", type=str, dest="additional_system_instructions", default="", help="Additional system instructions")

    args = parser.parse_args()

    # Example usage
    flags = generate_flags(theme=args.theme,
                           tone=args.tone, 
                           amt=args.amt, 
                           model=args.model, 
                           flag_format=args.flag,
                           response_format=args.response,
                           language=args.language,
                           category=args.category, 
                           tags=args.tags,
                           additional_flag_instructions=args.additional_flag_instructions,
                           additional_system_instructions=args.additional_system_instructions,
    )

    print(flags)

if __name__ == "__main__":
    main()

