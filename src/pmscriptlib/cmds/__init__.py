
from .exceptions import UsageError

from .InitCommand import InitCommand
from .ListProcessesCommand import ListProcessesCommand
from .ListCasesCommand import ListCasesCommand
from .ListVarsCommand import ListVarsCommand
from .SetVarCommand import SetVarCommand
from .ListTasksCommand import ListTasksCommand
from .ListStartsCommand import ListStartsCommand
# Import CMDs here

ALL_CMDS = [
    InitCommand(),
    ListProcessesCommand(),
    ListCasesCommand(),
    ListVarsCommand(),
    SetVarCommand(),
    ListTasksCommand(),
    ListStartsCommand(),
    # Add CMD class here
]
ALL_CMDS = {c.cmd_name: c for c in ALL_CMDS}
