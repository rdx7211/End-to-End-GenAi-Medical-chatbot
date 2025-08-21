import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb",
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")



#you u can use also bash commands to create the directory and files

# for instance

# code for bash one 

# # Creating directory 
# mkdir -p src
# mkdir -p research 

# # Creating files
# touch src/__init__.py
# touch src/helper.py 
# touch src/prompt.py
# touch .env 
# touch setup.py
# touch app.py
# touch research/trials.ipynb 
# touch requirements.txt


# echo "Directory and files created successfully!."
