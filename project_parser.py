"""
This is a YAMl parser that processes and visualizes a project in streamlit

general stucture:

```yaml
Project:
  Name: "E Commerce Platform"
  Description: "A platform to sell products"

  C_YourComponent:
    Template: "hub/tech_stack" # This will fetch a template for a specific tech stack,
    # a tech stack might be an express server or a react app or a flask server
    P_YourPart:
      Name: "What you call your part"
      Description: "What your part should do"
      Input:
        Type: "Object/String/Int"
        Description: "What your input is"
      Output:
        Type: "Object/String/Int"
        Description: "What your output is"
    GLUE:
      Code: "@/directory" # this is where your code for the specific tech stack will go
      # the route registration of anything else that interacts with the parts
      Description: "Glue code to hold together parts in the component"
      Dependencies: "..."
```

"""

import yaml
import streamlit as st
import os

# ask user to upload a project file
project_file = st.file_uploader("Upload a project file", type=["yaml", "yml"])

if project_file is None:
    st.stop()

# load the project file
project = yaml.safe_load(project_file)

# skip the project level
project = project["Project"]


st.title(project["Name"])
st.write(project["Description"])

import json
def process_IO(input):
    element = st.subheader(f"Name: {input['Name']}")
    st.write(input["Description"])

    # show an example of the input and showing the type in a nice and easily readable way

    st.markdown(f"**Type:** `{input['Type']}`")
    st.subheader("Example")
    try:
        # try to parse it as json and pretty print it
        st.write(json.dumps(json.loads(input["Value"]), indent=4))
    except:
        st.write(input["Value"])

    return element

def open_part_editor(part):
    # open a new page in streamlit
    st.title(part["Name"])
    st.write(part["Description"])

    # show the input and output
    with st.expander("Show Input"):
        input = part["Input"]
        input = process_IO(input)

    with st.expander("Show Output"):
        output = part["Output"]
        output = process_IO(output)

    # let the user start working on the part
    st.subheader("Code")
    code = st.code_editor(part["Code"])


for component in project:
    if component.startswith("C_"):
        st.header(project[component]["Name"])
        st.write(project[component]["Description"])
        part = "GLUE"

        st.subheader("Glue")
        st.write(project[component][part]["Description"])
        # get the graph
        graph = project[component][part]["Graph"]
        # syntax is like: a -> b -> c
        # plot it:
        graph = f"digraph G {{ {graph} }}"
        st.graphviz_chart(graph)
        for part in project[component]:
            if part.startswith("P_"):
                st.subheader(part[2:])
                st.write(project[component][part]["Description"])

                # hidden drop-down
                with st.expander("Show Input"):
                    input = project[component][part]["Input"]
                    input = process_IO(input)

                with st.expander("Show Output"):
                    output = project[component][part]["Output"]
                    output = process_IO(output)

            if part == "GLUE":
                pass


# show a TOC
st.sidebar.title("Project Structure")
for component in project:
    if component.startswith("C_"):
        st.sidebar.subheader(project[component]["Name"])
        for part in project[component]:
            if part.startswith("P_"):
                # make a link to the part, make lowercase and replace spaces with dashes
                link = part[2:].lower().replace(" ", "-")
                st.sidebar.write(f"- [{part[2:]}](#{link})")