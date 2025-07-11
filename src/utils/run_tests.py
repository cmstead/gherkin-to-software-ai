import subprocess

def run_tests(test_path):
    try:
        command = f"npm test"
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=test_path, shell=True)

        stdout = process.communicate()
        
        return stdout, process.returncode
    except Exception as e:
        print(f"An error occurred while running tests: {e}")
        return None, -1