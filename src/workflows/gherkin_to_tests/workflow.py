import os

from src.constants import SCRIPT_ROOT
from src.utils.fs import read_file, write_file

from src.workflows.gherkin_to_tests.steps.gherkin_to_jest import get_jest_tests

def run_test_build(feature_path, test_path):
    persona = read_file(f"{SCRIPT_ROOT}/ai_files/personas/software-developer.md")
    gherkin_spec = read_file(f"{os.getcwd()}/{feature_path}")
    
    jest_tests = get_jest_tests({
        "Gherkin": gherkin_spec,
        "Persona": persona
    })
    write_file(f"{os.getcwd()}/{test_path}", jest_tests)
    
    return True