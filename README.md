# CTF_Assets
Library to use LLMs to generate assets for CTF capture the flag challenges

Download the repository to a place in you system
git clone git@github.com:hallymag/CTF_Assets.git
cd CTF_Assets
# create and activate virtual environment
pyhton -m venv venv
# install requirements
pip install -r requirements.txt
# Since it is still in development install the package with:
#    **pip install -e <path to the source of the package>**
pip install -r requirements.txt

Since it is still in developmment, if you have already installed it, before using:
   - Pull the changes to the main branch to get updated code.

1. To use as a library just import the desired functions

2. To use from the Command Line (CLI):
sintax: ctf-assets <one of [flags, stories]> <one of [generate_flags,
generate_stories, generate_stories_with_titles]> <any of: [theme, tone,
amt, model, flag_format,language, additional_instructions, 
additional_system_instructions]> 

You can see the flags that can be used in the setup.py
---
Example use from the command prompt:

$ ctf-assets flags generate_flags --amt 5 --theme "Moon" --tone "funny" 
--flag-format upr{..} --additional-instructions "Flag responses are less or equal to 50 characters"

$ ctf-assets stories generate_stories --amt 2 --theme "Moon", --tone "informational" --additional-instructions "Stories  are less or equal to 100 words"

$ ctf-assets stories generate_stories_with_titles --amt 2 --theme "Moon", --tone "informational" --additional-instructions "Flag responses are less or equal to 50 characters"

-Flags are optional and have defaults. For example amt defaults to 1, flag-format defaults to ctf{..}

$ ctf-assets flags generate_flags




