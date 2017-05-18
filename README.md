pmscript
========

Script for interacting with a ProcessMaker server


Usage
-----

    usage: pmscript.py [-h] [--creds CREDS] {list_projects,init} ...
    
    Script for interacting with a ProcessMaker server
    
    optional arguments:
      -h, --help            show this help message and exit
      --creds CREDS         Path to credentials file to access the server
    
    commands:
      valid commands
    
      {list_projects,init}
        list_projects       List all of the projects (processes or workflows)
                            defined
        init                Initialize a new credentials file
