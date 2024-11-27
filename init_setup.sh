echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.8"
conda create --prefix ./env python=3.8 -y
echo [$(date)]: "activate env"
conda activate ./env
echo [$(date)]: "installing requirements"
echo [$(date)]:"present working directory"
pwd
pip install -r requirements.txt
echo [$(date) ]: "END"
#this file is used to run multiple terminal commands in one file