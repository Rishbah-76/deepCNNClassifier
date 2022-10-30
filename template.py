import os
import logging
from pathlib import Path

#logging config
logging.basicConfig(level=logging.INFO, format='[%(asctime)s] %(message)s')

#for basic skeleton filesystem
package_name="deepclassifier"
list_of_files=[
    "./github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "setup.py",
    "setup.cfg",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "pyproject.toml",
    "tox.ini",
    "research/trails.ipynb",
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir, filename=os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath) or (os.path.getsize(filepath) == 0)):
        with open(filepath,"w") as f:
            pass
        logging.info(f"Creating directory: {filedir}")
    else:
        logging.info(f"{filename} already exist")
