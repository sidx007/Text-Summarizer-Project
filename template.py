import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format = '[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/main.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/init.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "Dockerfile",
    "Dockerfile"
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_files:
    filepath = Path(filepath)
    filefir,filename = os.path.split(filepath)

    if filefir != "":
        os.makedirs(filefir, exist_ok=True)
        logging.info(f"Creating directory {filefir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file {filename}")

    else:
        logging.info(f"File {filename} already exists and is not empty. Skipping creation.")