import streamlit as st
from code_editor import code_editor

# parse url parameters to get the project and part
import urllib.parse
url = st.experimental_get_query_params()

arguments = {
    'project_path': url['project_path'][0],
    'project': url['project'][0],
    'component': url['component'][0],
    'part': url['part'][0]
}


def process_IO(input):
    # if we have Input: {} we have no imput so we can just return a
    if input == {}:
        return None
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

# load the project
import yaml
with open(arguments['project_path'], "r") as project_file:
    project = yaml.load(project_file, Loader=yaml.FullLoader)

project = project['Project']
for component in project:
    if component.startswith("C_"):
        if component[2:] == arguments['component']:
            for part in project[component]:
                if part.startswith("P_"):
                    if part[2:] == arguments['part']:
                        st.title(project[component][part]["Name"])
                        st.write(project[component][part]["Description"])

                        # show the input and output
                        with st.expander("Show Input"):
                            input = project[component][part]["Input"]
                            input = process_IO(input)

                        with st.expander("Show Output"):
                            output = project[component][part]["Output"]
                            output = process_IO(output)

                        # show the input and output
                        editor = code_editor("def fn():\n    pass",
                                             shortcuts='vim')

                        break
            break
# get the part



