# Create a virtual python environment called env (it creates a folder called env):

python3 -m env env/

# Enter virtual environment (this will place you in the virtual environment)

source env/bin/activate

At this point you will get a new prompt and all python package install commands will install packages relative/for to this environment only

# Installing packages (execute this while in virtual environment)

python3 -m pip install pygame

Note: -m looks like it reaches out to an external program like pip or venv etc

# Exit virtual environment

deactivate

Enter deaactivate while within the virtual environment to exit it. All package installs will then be installed system wide (generally not great)


# Resources

Read more about python virtual environments here: https://realpython.com/python-virtual-environments-a-primer/
