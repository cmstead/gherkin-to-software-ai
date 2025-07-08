import json

def read_file(file_path):
    f = open(file_path, 'r')
    content = f.read()
    f.close()

    return content

def read_json_file(file_path):
    json_content = None
    
    with open(file_path, "r") as file:
        json_content = json.load(file)
        
    return json_content

def write_file(file_path, content):
    f = open(file_path, 'w')
    f.write(content)
    f.close()