import yaml
import jsonschema

# Define the JSON schema
schema = {
    "type": "object",
    "properties": {
        "Project": {
            "type": "object",
            "properties": {
                "Name": {"type": "string"},
                "Description": {"type": "string"},
            },
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "Name": {"type": "string"},
                    "Description": {"type": "string"},
                    "GLUE": {"type": "object"},
                },
                "additionalProperties": {
                    "type": "object",
                    "properties": {
                        "Name": {"type": "string"},
                        "Description": {"type": "string"},
                        "Input": {"type": "object"},
                        "Output": {"type": "object"},
                    },
                    "required": ["Name", "Description", "Input", "Output"],
                },
                "required": ["Name", "Description", "GLUE"],
            },
            "required": ["Name", "Description"],
        },
    },
    "required": ["Project"],
}


import random
import string
import json

def generate_random_value(var_type):
    if var_type == "String":
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    elif var_type == "Number":
        return random.uniform(1, 100)
    elif var_type == "Int":
        return random.randint(1, 100)
    elif var_type == "Object":
        return json.dumps({"key": ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))})
    else:
        return None

def process_IO(input_dict):
    required_keys = ['Name', 'Description', 'Type']
    for key in required_keys:
        if key not in input_dict:
            input_dict[key] = input(f"{key} key not found in input. Please provide the {key}: ")
        print(f"{key}: {input_dict[key]}")
    if 'Value' not in input_dict:
        input_dict['Value'] = generate_random_value(input_dict['Type'])
        print(f"Value: {input_dict['Value']}")

# Load the YAML file
with open('../project.yaml', 'r') as file:
    project = yaml.safe_load(file)

# Validate the YAML file
try:
    jsonschema.validate(instance=project, schema=schema)
except jsonschema.exceptions.ValidationError as err:
    print(f"Validation error: {err}")
    exit(1)

# Process the input and output of each part of the project
for component in project["Project"]:
    if component.startswith("C_"):
        for part in project["Project"][component]:
            if part.startswith("P_"):
                process_IO(project["Project"][component][part]["Input"])
                process_IO(project["Project"][component][part]["Output"])

# Reformat the YAML file
with open('../project.yaml', 'w') as file:
    yaml.dump(project, file, default_flow_style=False, sort_keys=False)

print("The project definition is valid and has been reformatted.")