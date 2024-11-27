#this is the main file used to publish the local_package 
from setuptools import find_packages, setup

setup(
    name="my_package_name",  # Replace with your package name
    version="0.0.1",
    author="Ravi",
    author_email="ravikhichar9715@gmail.com",
    packages=find_packages(),  # Automatically discover and include all packages
    install_requires=[
        "langchain",  # List of external dependencies
        # Add other dependencies here, for example:
        # "numpy",
        # "pandas",
    ]
)