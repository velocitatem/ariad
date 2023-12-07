import sys
sys.path.append("../")
# data_reporter.py
from ariad import Ariad

proj = Ariad.register("demo_project")

def data_reporter(data):
    # Generate a detailed report of the data
    for item in data:
        print(f"ID: {item['id']}, Processed Value: {item['processed_value']}")

proj.register_module("data_reporter", data_reporter)
