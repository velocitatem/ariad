# main.py
from ariad import Ariad
from demo.data_loader import data_loader
from demo.data_processor import data_processor
from demo.data_reporter import data_reporter


if __name__ == "__main__":
    project = Ariad("demo_project")

    # Execute the modules in a sequence
    data = project.execute_module("data_loader")
    processed_data = project.execute_module("data_processor", data)
    project.execute_module("data_reporter", processed_data)

