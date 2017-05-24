import sys

from .Command import Command
from ..PMServer import PMServer
from .exceptions import UsageError

class SetVarCommand(Command):
    '''Set a case variable'''


    def add_cmdline_args(self, parser):
        '''Add commandline arguments specific to this command'''
        parser.add_argument('--process', help="Name or UID of the process to list cases for.")
        parser.add_argument('--case', help="Name or UID of the case to show variables for.")
        parser.add_argument('--var', help="Name of the variable to update.")
        parser.add_argument('--value', help="String value to set.")


    def run(self, args):
        '''Perform command actions'''

        creds = self._load_creds(args)
        server = PMServer(creds)

        # Check arguments
        if args.case is None:
            raise UsageError('--case is required')
        if args.var is None:
            raise UsageError('--var is required')
        if args.value is None:
            raise UsageError('--value is required')

        # Find requested case
        case = server.find_case(process=args.process, name=args.case)
        if case is None:
            print("ERROR: Couldn't find case '%s'" % (args.case))
            sys.exit(2)

        # Get current value
        print('Setting variable %s for case "%s" in process %s' % (args.var, case.name, case.process.name))
        try:
            print("Value of %s was '%s'" % (args.var, case.variables[args.var]))
        except KeyError:
            print("%s is not currently setup" % (args.var))

        # Set value
        case.set_variables({args.var: args.value})
        print("Set value to '%s'" % (args.value))

    