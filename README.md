### A simple Python project templator.
This is simple command line project developed using `click`, which helps to create files and directories for a new project.


#### Usage
Get Help.
```
$ project --help
Usage: project [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  create
  destroy
```

Create new project skeleton.
```
$ project create myNewProject --source source --tests tests --resources resources --basepath /home/myHome
########################################################################################################################
##### Project `myNewProject` created at location `/home/myHome/myNewProject` 
/home/myHome
├── __init__.py
├── Makefile
├── resources
│   └── __init__.py
├── setup.py
├── source
│   └── __init__.py
└── tests
    └── __init__.py

3 directories, 6 files

```

Destroying the created project.
```
$ project destroy myNewProject --basepath /home/anirudh
Deleting project `myNewProject` from location `/home/anirudh/myNewProject` ....
Deleted
```
