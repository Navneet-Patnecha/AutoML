import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project_name = 'automl_project'

# Define the file structure
file_structure = [
    f"{project_name}/data/raw/.gitkeep",
    f"{project_name}/data/processed/.gitkeep",
    f"{project_name}/notebooks/data_ingestion.ipynb",
    f"{project_name}/notebooks/eda.ipynb",
    f"{project_name}/notebooks/model_training.ipynb",
    f"{project_name}/reports/eda_report.pdf",
    f"{project_name}/src/data_preprocessing.py",
    f"{project_name}/src/model_training.py",
    f"{project_name}/src/utils.py",
    #f"{project_name}/requirements.txt",
    #f"{project_name}/main.py",
    f"src/{project_name}/exception.py",
    f"src/{project_name}/logger.py",
    f"src/{project_name}/utils.py"
]

def create_file_structure():
    for filepath in file_structure:
        filepath = Path(filepath)
        filedir, filename = os.path.split(filepath)

        if filedir:
            os.makedirs(filedir, exist_ok=True)
            logging.info(f"Creating directory: {filedir}")

        if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
            if filename == ".gitkeep":
                with open(filepath, 'w') as f:
                    pass
            logging.info(f"Creating empty file: {filepath}")
        else:
            logging.info(f"{filepath} already exists")

if __name__ == "__main__":
    create_file_structure()