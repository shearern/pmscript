
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
        for proj in server.list_projects():
            print(proj.name)
