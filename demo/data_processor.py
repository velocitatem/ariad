import sys
sys.path.append("../")
# data_processor.py
from ariad import Ariad

proj = Ariad.register("demo_project")

def data_processor(data):
    # More complex data processing
    return [{"id": item["id"], "processed_value": item["value"] * 2} for item in data]

proj.register_module("data_processor", data_processor)
