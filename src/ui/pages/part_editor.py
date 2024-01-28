import streamlit as st
from code_editor import code_editor
# gotta get from from ../../builder/developer -- generate_code
import sys
gen_code = None
sys.path.append("src/builder/")
from developer import yaml_text_to_code
# reset path
sys.path.pop()
sys.path.append('src/')
from db import DB

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


def generate_default_code(name, description, inputObj, outputObj):
    func_name = name.replace(" ", "_")
    type_parser = lambda t: 'str' if 'str' in t else 'int' if 'int' in t else 'float' if 'float' in t else 'bool' if 'bool' in t else 'dict' if ('dict' in t or 'Object' in t) else 'list' if 'list' in t else 'str'
    input_string = f"{inputObj['Name']}: {type_parser(inputObj['Type'])}"
    output_string = f"{type_parser(outputObj['Type'])}"

    code = f"@part(\"{name}\")\ndef {func_name}({input_string}) -> {output_string}:\n\t\"\"\"{description}\"\"\"\n\tpass"
    return code


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
                        existing_code = generate_default_code(project[component][part]["Name"],
                                                              project[component][part]["Description"],
                                                                project[component][part]["Input"],
                                                                project[component][part]["Output"])
                        db = DB()
                        code = db.get_latest_code(part)
                        print(code)
                        if code is not None:
                            existing_code = code[2]
                        editor = code_editor(existing_code,
                                             shortcuts='vim')
                        yaml_of_part = project[component][part]
                        # to yaml format:
                        yaml_of_part = yaml.dump(yaml_of_part)
                        # button to generate code
                        if st.button("Generate Suggestions"):
                            markdown = yaml_text_to_code(yaml_of_part)
                            markdown = markdown.choices[0].message.content
                            # put markdown in toggleable expander
                            with st.expander("Suggestions"):
                                st.markdown(markdown)

                        #  submit:
                        if st.button("Save"):
                            code = editor['text']
                            db.add_part(part, part, code)
                            st.balloons()
                            st.success("Saved!")



                        break
            break
# get the part



