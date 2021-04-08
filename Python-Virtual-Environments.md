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

# List installed packages
To list the installed packages: **pip list**  
Or similar: **pip freeze**

# Keep track of requirements 
*   You can keep track of requirements by saving the list to a file called **"requirements.txt"**.
**pip freeze > requirements.txt**
*   And each time you update a package you will run the same command.