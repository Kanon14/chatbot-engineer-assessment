import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    ".github/workflows/.gitkeep",
    ".streamlit/config.toml",
    ".env",
    "agent/__init__.py",
    "agent/workflow.py",
    "config/__init__.py",
    "config/config.yaml",
    "exception/__init__.py",
    "logger/__init__.py",
    "prompt_library/__init__.py",
    "prompt_library/prompt.py",
    "utils/__init__.py",
    "tools/__init__.py",
    "notebook/experiment.ipynb", 
    "main.py",
    "agent.py",
    "streamlit_app.py",
    "requirements.txt",
    "setup.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    if (not os.path.exists(filename)) or (os.path.getsize(filename) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")    
    else:
        logging.info(f"File already exists: {filename}")