
from .exceptions import UsageError

from .InitCommand import InitCommand
from .ListProjectsCommand import ListProjectsCommand
from .ListCasesCommand import ListCasesCommand

ALL_CMDS = [
    InitCommand(),
    ListProjectsCommand(),
    ListCasesCommand(),
]
ALL_CMDS = {c.cmd_name: c for c in ALL_CMDS}