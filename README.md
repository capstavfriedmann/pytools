<h1>Repo for python script utilities</h1>

<h4>Usage:</h4>
1. Create a new empty directory
2. run: git clone git@github.com:capstavfriedmann/pytools.git .
3. ensure make is installed (pip install make)
4. run: make setup tool1 tool2 .....

<h4>Description:</h4>

This repository is designed to setup a clean working space for python projects following this filstructure

project_name:
|_src:
|_test:
|_pytools:
Makefile
README.md
.gitignore

The Makefile is preconfigured to checkout a list of feature branches, each containing a tool folder in its pytools folder. It will create a new temporary branch, merge each feature in turn, and then orphan itself from git, giving the user just the bare tools and filestructure.


<h4>Extension:</h4>

To add a tool:
    1. git checkout master
    2. git checkout -b <tool-name>
    3. cd ./pytools
    4. mkdir <tool-name>
    5. cp /path/to/self-contained/tool/folder ./<tool-name>/
    6. git add ./tool-name
    7. git add -u origin <tool-name>
    8. git push

Or in plain english, add your tool folder to pytools and push to a branch containing only that tool