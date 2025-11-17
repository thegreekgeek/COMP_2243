# COMP_2243

## DESCRIPTION

Colab Projects for RCTC's COMP2243, taught by [Brendan Shea](https://github.com/brendanpshea). The repository for the class is added as a git submodule. This repository contains a script that will extract all the java programming exercises from the notebooks and save them as .java files in a seperate folder.

## TO FORK PROJECT
For the uninitiated, /forking/ a project is basically creating your own copy of the repository with the edit history preserved. On the top of the page next to the star icon, there'll be a "Fork" button. Click that. You'll need to be logged into github, which is encouraged because git is awesome.

If you don't have a github and you don't want to create one you can clone the repository and change the remote to point to a git repository of your choosing. This might be added to the just file for ease of use.

## TO RUN SCRIPT

If running via the command line, navigate to the project root (COMP_2243). In that folder, run the command:

```bash
python3 PracticeQuestionExtractor.py
```

## TODO

- Add a [justfile](https://just.systems) containing the commands to run this in windows and linux.
- Include a one-liner to install git?
