from src.utils.fs import read_file, write_file

from src.agents.gherkin_to_software.steps.gherkin_to_jest import get_jest_tests
from src.agents.gherkin_to_software.steps.jest_to_software import get_draft_code
# from src.agents.debug_software.debug_failed_tests import debug_failing_tests

def run_software_build(feature_name):
    persona = read_file("ai_files/personas/software-developer.md")
    #read gherkin
    gherkin_spec = read_file(f"_source_input/{feature_name}.feature")
    
    #get jest code
    jest_tests = get_jest_tests({
        "Gherkin": gherkin_spec,
        "Persona": persona
    })
    write_file(f"_result_output/{feature_name}.spec.js", jest_tests)

    #get production code
    draft_code = get_draft_code({
        "Jest": jest_tests,
        "Persona": persona
    })
    #write code to file
    write_file(f"_result_output/{feature_name}.js", draft_code)
    
    #run test suite
    # import subprocess
    # mainPath = r"filepath"
    # command = 'whatever'
    # subprocess.Popen('start cmd /k '+ command,cwd=mainPath,shell=True)

    #debug failing tests as necessary
    #write debugged code to file
    
    return True