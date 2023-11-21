<h1>Repo for python script utilities</h1>

<h4>Usage:</h4>
<ol>
<li> Create a new empty directory </li>
<li> run: git clone git@github.com:capstavfriedmann/pytools.git . </li>
<li> ensure make is installed (pip install make) </li>
<li> run: make setup tool1 tool2 ..... </li>
</ol> 
<h4>Description:</h4>

This repository is designed to setup a clean working space for python projects following this filstructure<p>

project_name: <br>
|_src:<br>
|_test:<br>
|_pytools:<br>
Makefile<br>
README.md<br>
.gitignore<br>
.env<br>
<p>
The Makefile is preconfigured to merge a list of feature branches, each containing a tool folder in its pytools folder by creating a new temporary branch, merging each feature in turn, and then orphaning itself from git. This has the effect of giving the user just the bare tools and filestructure. The file will also load any environment variables from .env (useful for sensitive information in API calls)

NB: This is boilerplate for development purposes, code inside src/ should run independently of everything in this repository

<h4>Extension:</h4>

To add a tool:
<ol>
    <li> git checkout master </li>
    <li> git checkout -b *tool-name* </li>
    <li> mkdir ./pytools/*tool-name* </li>
    <li> cp /path/to/self-contained/tool/folder/* ./pytools/*tool-name*/ </li>
    <li> git add ./pytools/*tool-name* </li>
    <li> git add -u origin *tool-name* </li>
    <li> git push </li>
</ol>

Or in plain english, add your tool folder to pytools and push to a branch containing only that tool
