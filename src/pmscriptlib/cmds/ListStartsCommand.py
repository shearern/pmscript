
from tabulate import tabulate

from .Command import Command
from ..PMServer import PMServer

class ListStartsCommand(Command):
    '''List start tasks that can be invoked by the user'''


    def add_cmdline_args(self, parser):
        '''Add commandline arguments specific to this command'''
        parser.add_argument('--process', help="Name or UID of the process to list tasks for.")


    def run(self, args):
        '''Perform command actions'''

        creds = self._load_creds(args)
        server = PMServer(creds)

        tasks = list()
        for process in server.list_processes():
            if self._matches_process_arg(process, args):
                tasks.extend(list(process.list_start_tasks()))

        print(tabulate(
            [(task.name, process.name, task.uid) for task in tasks],
            headers=['Task', 'Process', 'Task UID']
        ))


    def _matches_process_arg(self, task, args):

        if args.process is None:
            return True

        # Name match
        if task.process.name == args.process:
            return True

        # UID match
        if len(args.process) >= 6:
            if task.process.uid.startswith(args.process):
                return True
            if task.process.uid.endswith(args.process):
                return True

        return False


