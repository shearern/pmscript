pmscript
========

Script for interacting with a ProcessMaker server


Usage
-----

    usage: pmscript.py [-h] [--creds CREDS]
                       {list_processes,list_cases,init,list_vars} ...
    
    Script for interacting with a ProcessMaker server
    
    optional arguments:
      -h, --help            show this help message and exit
      --creds CREDS         Path to credentials file to access the server
    
    commands:
      valid commands
    
      {list_processes,list_cases,init,list_vars}
        list_processes      List all of the projects (processes or workflows)
                            defined
        list_cases          List cases
        init                Initialize a new credentials file
        list_vars           Show the current variable values for a case

