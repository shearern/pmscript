from tabulate import tabulate

from ..PMServer import PMServer

from .Command import Command

class ListCasesCommand(Command):
    '''List cases'''


    def add_cmdline_args(self, parser):
        '''Add commandline arguments specific to this command'''
        parser.add_argument('--process', help="Name or UID of the process to list cases for.")
        parser.add_argument('--active', help="Show only active cases", action='store_true')


    def run(self, args):
        '''Perform command actions'''
        creds = self._load_creds(args)
        server = PMServer(creds)

        rows = list()
        for case in server.list_cases():
            rows.append((
                case.title,
                case.process.name,
                case.uid,
            ))
        print(tabulate(rows, headers=["Title", "Process", 'UID']))


    