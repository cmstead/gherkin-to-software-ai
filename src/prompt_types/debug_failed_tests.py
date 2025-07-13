from src.constants import SCRIPT_ROOT
from src.utils.fs import read_file

PROMPT_FIELDS = [
    "Persona",
    "Source Code",
    "Unit Tests",
    "Debug Output"
]

def get_prompt():
    return read_file(f"{SCRIPT_ROOT}/ai_files/prompts/debug-failed-tests.md")