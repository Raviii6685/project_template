#this is a resusable file
import os
from pathlib import Path
while True:
    project_name = input("Enter the Src Folder Name:")
    if project_name != "":
        break

#we have created the folder structure of this project dynamic
#this is 95% blue print must needed
list_of_files = [
            "github/workflows/.gitkeep" , #helps to push an empty otherwise folder
            #its just like pass keyword , its helps to push the empty folder also (wuithout the complications)
            f"{project_name}/__init__.py", #Marks the directory as a Python package.
            f"{project_name}/ components/data_ingestion.py",#Handles data collection and loading from external sources like databases, APIs, or local files.
            f"{project_name}/components/data_preproceesing.py", #Prepares raw data for training/testing, including cleaning, normalization, augmentation, and splitting.
            f"{project_name}/components/model_loading.py",#Loads pre-trained models or initializes new architectures.
            f"{project_name}/components/model_evaluation.py",#Evaluates model performance using metrics like accuracy, precision, recall, F1-score, etc
            f"{project_name}/pipeline/inference.py", #Facilitates making predictions on unseen data.
            f"{project_name}/pipeline/training.py", #Automates the training pipeline, including data feeding, model training, validation, and checkpoint saving.
            f"{project_name}/exception.py", #Defines custom exceptions for handling errors specific to the project.
            f"{project_name}/logger.py",#Provides structured logging for tracking events, metrics, and errors.
            "templates/index.html",#Template for rendering the web interface using Flask/Django (or similar frameworks).
            "statics/style.css"
            "notebook/research.ipynb",
            "init_setup.sh",#Shell script to initialize the project environment (e.g., installing dependencies, setting up virtual environments).
            "requirements. txt",# Lists Python dependencies required for the project.
            "Dockerfile",#Contains instructions to create a Docker image for the project.
            "app.py",# Main entry point for the application (e.g., serving a Flask app or running the ML model).
            "setup.py"#Defines the metadata and configuration for packaging the project as a Python library.
]

for filepath in list_of_files:
    file_path = Path(filepath)
    filedir,filename=os.path.split(file_path)
    if filedir !="":
         os.makedirs(filedir,exist_ok=True)
    if not os.path.exists(file_path):
        with open(file_path, 'a') as f:
            pass