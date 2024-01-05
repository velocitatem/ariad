import streamlit as st
import time
import sys
sys.path.append("../")
from ariad import Ariad

def toggle_valve(valve_component):
    # toggle every 5 seconds
    desc = lambda s: "Open" if s else "Closed"
    tt = False
    status = st.write(desc(tt))
    for i in range(10):
        time.sleep(1)
        status=st.write(desc(tt))
        valve_component.toggle_state()
        tt= not tt


# Register the new module function with Ariad
proj = Ariad.register("valves")
proj.register_module("toggle_valve", toggle_valve)

if __name__ == "__main__":
    # Create a valve component
    # test out the new module function
    class Valve:
        def __init__(self):
            self.state = "closed"

        def toggle_state(self):
            if self.state == "closed":
                self.state = "open"
            else:
                self.state = "closed"

    valve = Valve()
    if st.button("Toggle Valve"):
        toggle_valve(valve)

