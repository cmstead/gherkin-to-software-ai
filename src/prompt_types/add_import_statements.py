from src.utils.fs import read_file

PROMPT_FIELDS = [
    "Persona",
    "File Path",
    "Source",
    "Jest"
]

def get_prompt():
    return read_file("ai_files/prompts/add-import-statements.md")