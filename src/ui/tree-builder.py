"""
this is a python script that makes use of streamlit to build a tree of modules
that can be executed in order. Say we are building a machine learning model.
We might want to have a module that loads the data, a module that processes the data,
a module that trains the model, and a module that reports the results.

The purpose is to show a bottom up and top down view of the project.
In this program we let user create functions(modules) and their dependencies aswell
as inputs and outputs.
When a user clicks on a module the program will show the user the inputs and outputs of that module.
"""

# we dont need ariad in this file, its just to overview the project

# ui/tree-builder.py
# ui/tree-builder.py

# ui/tree-builder.py

# ui/tree-builder.py
# ui/tree-builder.py
import streamlit as st
import pandas as pd
from pyvis.network import Network
import streamlit.components.v1 as components

# ui/tree-builder.py
import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

import networkx as nx
import matplotlib.pyplot as plt

def create_plot(data):
    # Create a graph
    G = nx.DiGraph()

    # Add nodes
    for node in data:
        G.add_node(node)

    # Add edges
    for node, info in data.items():
        for dependency in info["dependencies"]:
            G.add_edge(dependency, node)

    # Create a shell layout with nodes ordered by their number of dependencies
    shell_layout = [sorted(G.nodes(), key=lambda x: len(data[x]["dependencies"]))]

    # Draw the graph
    plt.figure(figsize=(10, 10))
    nx.draw(G, pos=nx.shell_layout(G, shell_layout), with_labels=True)
    plt.show()

def main():
    st.title('Project Tree Builder')

    # Initialize the session state if it doesn't exist
    if "modules" not in st.session_state:
        st.session_state.modules = {
            "data_loader": {"inputs": [], "outputs": ["data"], "dependencies": []},
            "data_processor": {"inputs": ["data"], "outputs": ["processed_data"], "dependencies": ["data_loader"]},
            "model_trainer": {"inputs": ["processed_data"], "outputs": ["model"], "dependencies": ["data_processor"]},
            "results_reporter": {"inputs": ["model"], "outputs": [], "dependencies": ["model_trainer"]},
        }


    # Create a DataFrame from the modules dictionary and display it
    modules_df = pd.DataFrame.from_dict(st.session_state.modules, orient='index')
    st.dataframe(modules_df)

    with st.expander("Add a new module"):
        new_module_name = st.text_input("Module name")
        new_module_inputs = st.text_input("Inputs (comma-separated)")
        new_module_outputs = st.text_input("Outputs (comma-separated)")
        new_module_dependencies = st.text_input("Dependencies (comma-separated)")

        if st.button("Add module"):
            # add all the children (dependencies) first to make sure they exist
            for dependency in new_module_dependencies.split(","):
                if dependency not in st.session_state.modules:
                    st.session_state.modules[dependency] = {
                        "inputs": [],
                        "outputs": [],
                        "dependencies": [],
                    }

            st.session_state.modules[new_module_name] = {
                "inputs": new_module_inputs.split(","),
                "outputs": new_module_outputs.split(","),
                "dependencies": new_module_dependencies.split(","),
            }
            st.write(f"Module {new_module_name} added")
            st.experimental_rerun()

    with st.expander("Plot the project tree"):
        st.set_option('deprecation.showPyplotGlobalUse', False)
        plot=create_plot(st.session_state.modules)
        st.pyplot(plot)

if __name__ == "__main__":
    main()