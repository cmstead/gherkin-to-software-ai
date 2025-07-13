from src.constants import SCRIPT_ROOT
from src.utils.fs import read_file
PROMPT_FIELDS = [
    "Persona",
    "File Path",
    "Source",
    "Jest"
]

def get_prompt():
    return read_file(f"{SCRIPT_ROOT}/ai_files/prompts/add-import-statements.md")