# COMP_2243

## DESCRIPTION

Colab Projects for RCTC's COMP2243, taught by [Brendan Shea](https://github.com/brendanpshea). The repository for the class is added as a git submodule. This repository contains a script that will extract all the java programming exercises from the notebooks and save them as .java files in a seperate folder.

## TO FORK PROJECT
For the uninitiated, /forking/ a project is basically creating your own copy of the repository with the edit history preserved. On the top of the page next to the star icon, there'll be a "Fork" button. Click that. You'll need to be logged into github, which is encouraged because git is awesome.

If you don't have a github and you don't want to create one you can clone the repository and change the remote to point to a git repository of your choosing. This might be added to the just file for ease of use.

## TO GET STARTED

So  you'll need to do a little bit of setup. 

First, you'll actually need to download the files here. It's pretty easy to do, just click the green "Code" button and select "Download ZIP". Extract the files to a location of your choice.

Second, you'll need to make sure that Just is installed. It's pretty easy to do on windows, just use the keys WIN+R and type "powershell" and press enter. Then on the window that appears, type 

```code
winget install Casey.Just
```
and press enter.

You can close that terminal window and open a windows explorer window.

Next, you'll need to navigate to the project root (the folder that was in the zip file and now in your filesystem). In that folder, right click on an empty space and select "Open in terminal". Then in the window that appears, type the command:
```code
just first_run
```

This will download the other requirements like python and git if you don't already have them installed, then pull the latest version of the programming and problem solving git repository. Once it's downloaded it'll run the python script that extracts the code and pops it into java files organized by lecture. 

## TODO

- Add a [justfile](https://just.systems) containing the commands to run this in windows and linux.
- Include a one-liner to install git?
