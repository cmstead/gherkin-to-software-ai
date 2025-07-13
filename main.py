import inquirer

from src.constants import CWD
from src.workflows.gherkin_to_tests.workflow import run_test_build

def main():
    results = inquirer.prompt([
        inquirer.Text("feature_name", message="Enter the feature name:", default="feature_name"),
        inquirer.Text("feature_path", message="Enter path to feature files:", default="features"),
        inquirer.Text("test_path", message="Enter path to test files:", default="__tests__")
    ])
    
    feature_file_path = f"{CWD}/{results['feature_path']}/{results['feature_name']}.feature"
    feature_test_path = f"{CWD}/{results['test_path']}/{results['feature_name']}.spec.js"
    
    run_test_build(feature_file_path, feature_test_path)

if __name__ == "__main__":
    main()