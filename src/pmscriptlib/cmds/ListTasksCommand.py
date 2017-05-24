
from tabulate import tabulate

from .Command import Command
from ..PMServer import PMServer
from .exceptions import UsageError

class ListTasksCommand(Command):
    '''List tasks that are waiting to be performed'''


    def add_cmdline_args(self, parser):
        '''Add commandline arguments specific to this command'''
        parser.add_argument('--process', help="Name or UID of the process to list tasks for.")
        parser.add_argument('--case', help="Name or UID of the case to list tasks for.")


    def _list_cases_to_use(self, server, args):
        '''Find cases to search for tasks for'''

        # Find cases that match parameters
        for case in server.list_cases():

            if args.case is not None:

                # Check name matches
                if case.name != args.case:

                    # Check UID matches
                    if len(args.case) >= 6 and (case.uid.startswith(args.case) or case.uid.endswith(args.case)):
                        pass
                    else:
                        continue # Skip case

            if args.process is not None:
                prc = case.process

                # Check name matches
                if prc.name != args.process:

                    # Check UID matches
                    if len(args.process) >= 6 and (prc.uid.startswith(args.process) or prc.uid.endswith(args.process)):
                        pass
                    else:
                        continue # Skip case

            yield case


    def run(self, args):
        '''Perform command actions'''

        creds = self._load_creds(args)
        server = PMServer(creds)

        for case in self._list_cases_to_use(server, args):
            print('Case "%s" in process %s:' % (case.name, case.process.name))

            rows = list()
            for task in case.list_current_tasks():

                if task.started:
                    started = 'yes'
                else:
                    started = 'no'

                rows.append([
                    task.name,
                    task.type,
                    task.description,
                    task.username,
                    started,
                    task.status,
                    task.uid,
                ])

            print(tabulate(rows, headers=[
                'Name', 'Type', 'Description', 'Assigned', 'Started', 'Status', "UID"]))


    