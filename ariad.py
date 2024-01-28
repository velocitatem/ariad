import sys
from pathlib import Path

# Add src directory to Python path
src_dir = str(Path(__file__).resolve().parent)
if src_dir not in sys.path:
    sys.path.insert(0, src_dir)

# Now you can import any module from the src directory
from decorators import component, part
from argparse import ArgumentParser
from streamlit.web import cli as stcli
import sys
def main():
    """
    commands:
    ariad init - runs streamlit app in builder/ui.py
    ariad code - runs streamlit app in ui/project_parser.py
    :return:
    """
    parser = ArgumentParser()
    parser.add_argument("command", help="the command to run")
    args = parser.parse_args()
    if args.command == "init":
        sys.argv = ["streamlit", "run", "src/builder/ui.py"]
        sys.exit(stcli.main())
    elif args.command == "code":
        sys.argv = ["streamlit", "run", "src/ui/project_parser.py"]
        sys.exit(stcli.main())
    else:
        print("Unknown command")
if __name__ == "__main__":
    main()

