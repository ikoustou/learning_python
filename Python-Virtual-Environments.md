# How to install and create Virtual Environments with python >3.3 on Git Bash
*   Check python path: **which python**
*   Create a virtual envirnment named *env*: **python -m venv env**

# Activate virtual env
*   Activate the virtual environment running the **activate** file from bin (Linux) or Scripts (Windows):
**source ./env/Scripts/activate**
*   You will see the name of the virtual environment inside parenthesis **(env)** on the prompt.

#   How to install packages
The packages will be installed inside the folder: **Lib/site-packages.
To install a python package run:
**python -m pip install requests**

# Leaving the virtual environment
To deactivate the virtual environment simply run: **deactivate**