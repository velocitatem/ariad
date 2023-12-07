import sys
sys.path.append("../")
from ariad import Ariad

proj = Ariad.register("demo_project")


def data_loader():
    # Simulate a more complex data loading process
    data = []
    for i in range(1, 6):
        data.append({"id": i, "value": i})
    return data

proj.register_module("data_loader", data_loader)
