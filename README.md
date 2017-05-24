pmscript
========

Script for interacting with a ProcessMaker server


Usage
-----

    usage: pmscript.py [-h] [--creds CREDS]
                       
                       {set_var,list_processes,init,list_cases,list_tasks,list_vars}
                       ...
    
    Script for interacting with a ProcessMaker server
    
    optional arguments:
      -h, --help            show this help message and exit
      --creds CREDS         Path to credentials file to access the server
    
    commands:
      valid commands
    
      {set_var,list_processes,init,list_cases,list_tasks,list_vars}
        set_var             Set a case variable
        list_processes      List all of the projects (processes or workflows)
                            defined
        init                Initialize a new credentials file
        list_cases          List cases
        list_tasks          List tasks that are waiting to be performed
        list_vars           Show the current variable values for a case
