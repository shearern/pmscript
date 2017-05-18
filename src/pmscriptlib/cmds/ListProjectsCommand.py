
from tabulate import tabulate

from .Command import Command

from ..PMServer import PMServer

class ListProjectsCommand(Command):
    '''List all of the projects (processes or workflows) defined'''


    def add_cmdline_args(self, parser):
        '''Add commandline arguments specific to this command'''
        pass


    def run(self, args):
        '''Perform command actions'''
        creds = self._load_creds(args)
        server = PMServer(creds)

        rows = list()
        for proj in server.list_projects():
            rows.append((
                proj.name,
                proj.status,
                proj.uid))
        print(tabulate(rows, headers=["Name", "Status", "UID"]))
