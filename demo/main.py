# main.py
import streamlit as st
import sys
sys.path.append("../")
from ariad import Ariad
import pandas as pd


def main():
    project = Ariad("demo_project")

    st.title('Ariad Project Demo')

    stage1 = True
    stage2 = False
    stage3 = False
    if st.button('Load Data') or stage1:
        data = project.execute_module("data_loader")
        st.dataframe(data)  # Display the loaded data in a table
        stage2 = True

        if st.button('Process Data') or stage2:
            processed_data = project.execute_module("data_processor", data)
            st.dataframe(processed_data)
            stage3 = True

            if st.button('Report Data'):
                r=project.execute_module("data_reporter", processed_data)
                st.write("Data reported!")
                st.dataframe(r)


if __name__ == "__main__":
    main()