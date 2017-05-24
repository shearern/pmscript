import sys

from tabulate import tabulate

from .Command import Command
from ..PMServer import PMServer
from .exceptions import UsageError

class ListVarsCommand(Command):
    '''Show the current variable values for a case'''

    SYSTEM_VARS = set([
        'PIN',
        'PROCESS',
        'SESSION',
        'APPLICATION',
        'APP_NUMBER',
        'USR_USERNAME',
        'TASK',
        'SYS_LANG',
        'SYS_SYS',
        'INDEX',
        'USER_LOGGED',
        'SYS_SKIN',
        ])

    def add_cmdline_args(self, parser):
        '''Add commandline arguments specific to this command'''
        parser.add_argument('--process', help="Name or UID of the process to list cases for.")
        parser.add_argument('--case', help="Name or UID of the case to show variables for.")
        parser.add_argument('--show_sys', help="Show system variables", action='store_true')


    def run(self, args):
        '''Perform command actions'''

        creds = self._load_creds(args)
        server = PMServer(creds)

        # Check arguments
        if args.case is None:
            raise UsageError('--case is required')

        # Find requested case
        case = server.find_case(process=args.process, name=args.case)
        if case is None:
            print("ERROR: Couldn't find case '%s'" % (args.case))
            sys.exit(2)

        # Collect variables
        vars = case.variables

        # Print out variables
        print('Variables for case "%s" in process %s' % (case.name, case.process.name))
        print(tabulate([(k, v) for (k, v)
                        in sorted(vars.items(), key=lambda t: t[0].lower())
                        if (args.show_sys or k.upper() not in self.SYSTEM_VARS)]))

    