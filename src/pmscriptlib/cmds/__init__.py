
from .exceptions import UsageError

from .InitCommand import InitCommand
from .ListProjectsCommand import ListProjectsCommand

ALL_CMDS = [
    InitCommand(),
    ListProjectsCommand(),
]
ALL_CMDS = {c.cmd_name: c for c in ALL_CMDS}