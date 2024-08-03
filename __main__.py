import sys
import os
from streamlit.web import cli as stcli

def resolve_path(relative_path):
    """
    Resolves the given relative path to an absolute path.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, relative_path)

if __name__ == "__main__":
    # Resolve the path to the main.py file
    main_py_path = resolve_path("FantaAnalisi.py")

    # Set up sys.argv
    sys.argv = ["streamlit", "run", main_py_path]

    # Run Streamlit
    sys.exit(stcli.main())
