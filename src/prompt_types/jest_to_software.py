from src.utils.fs import read_file

PROMPT_FIELDS = [
    "Persona",
    "Jest"
]

def get_prompt():
    return read_file("ai_files/prompts/jest-to-software.md")