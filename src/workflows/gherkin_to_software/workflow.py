from src.constants import SCRIPT_ROOT
from src.utils.run_tests import run_tests
from src.utils.fs import read_file, write_file

from src.workflows.gherkin_to_tests.steps.gherkin_to_jest import get_jest_tests
from src.workflows.gherkin_to_software.steps.jest_to_software import get_draft_code
from src.workflows.gherkin_to_software.steps.add_import_statements import add_import_statements
from src.workflows.debug_software.steps.debug_failed_tests import debug_failing_tests

def run_software_build(feature_name):
    base_path = "_result_output/"
    file_name = f"{feature_name}.js"
    test_fileName = f"{feature_name}.spec.js"

    test_path = f"{base_path}{test_fileName}"
    file_path = f"{base_path}{file_name}"

    persona = read_file(f"{SCRIPT_ROOT}/ai_files/personas/software-developer.md")
    gherkin_spec = read_file(f"_source_input/{feature_name}.feature")
    
    jest_tests = get_jest_tests({
        "Gherkin": gherkin_spec,
        "Persona": persona
    })
    write_file(test_path, jest_tests)

    draft_code = get_draft_code({
        "Jest": jest_tests,
        "Persona": persona
    })
    write_file(file_path, draft_code)

    jest_tests = add_import_statements({
        "Persona": persona,
        "Source": draft_code,
        "Jest": jest_tests,
        "File Path": f"./{file_name}"
    })
    write_file(test_path, jest_tests)

    #run test suite
    stdout, exit_code = run_tests(base_path)
    
    if(stdout == None):
        return False
    
    if(exit_code):
        rerun_count = 5
        updated_code = draft_code
        
        while rerun_count > 0 and exit_code:
            print(f"Tests failed, rerunning... {rerun_count} attempts left.")
            rerun_count -= 1
            
            #debug failing tests
            updated_code = debug_failing_tests({
                "Persona": persona,
                "Source Code": draft_code,
                "Debug Output": stdout.decode('utf-8'),
                "Unit Tests": jest_tests,
            })
            
            stdout, exit_code = run_tests(base_path)
            print(stdout.decode('utf-8'))
            
            if exit_code == 0:
                break
        
        write_file(file_path, updated_code)

        print(stdout.decode('utf-8'))
    else:
        print('All tests passed successfully.')

    
    return True