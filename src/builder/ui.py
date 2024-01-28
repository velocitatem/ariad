import streamlit as st
from code_editor import code_editor

from architect import define_project
from developer import generate_code

# get projec title and desc from user
st.title("New Project")
project_name = st.text_input("Project Name")
project_desc = st.text_area("Project Description")
# session state streamlit to keep track of the project
st.session_state['set_project'] = False

if st.button("Create Project"):
    # show loading bar
    with (st.spinner("Creating Project")):

        definition = define_project(project_name, project_desc)
        def_path = definition

    # show the project
    with open(definition, "r") as definition_file:
        definition = definition_file.read()
    # open yaml in code editor
    view=code_editor(definition, lang="yaml")
    # save to session state
    st.session_state['definition'] = definition
    st.session_state['def_path'] = def_path
    st.session_state['set_project'] = True


if st.session_state['set_project']:
    if st.button("Generate Code"):
        definition = st.session_state['definition']
        def_path = st.session_state['def_path']
        with st.spinner("Generating Code"):
            res=generate_code(def_path)
            st.session_state['res'] = res
        st.write("Code Generated")
        st.balloons()
        res = st.session_state['res']
        with open(res, "r") as code_file:
            code = code_file.read()
            st.markdown(code)

