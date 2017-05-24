
from .exceptions import UsageError

from .InitCommand import InitCommand
from .ListProcessesCommand import ListProcessesCommand
from .ListCasesCommand import ListCasesCommand
from .ListVarsCommand import ListVarsCommand

ALL_CMDS = [
    InitCommand(),
    ListProcessesCommand(),
    ListCasesCommand(),
    ListVarsCommand(),
]
ALL_CMDS = {c.cmd_name: c for c in ALL_CMDS}
