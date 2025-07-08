from src.utils.fs import read_file

PROMPT_FIELDS = [
    "Persona",
    "Source Code",
    "Unit Tests",
    "Debug Output"
]

def get_prompt():
    return read_file("ai_files/prompts/debug-failed-tests.md")