
from .exceptions import UsageError
from .Command import Command
from ..PMServer import PMServer

class StartProcessCommand(Command):
    '''Create a new case to start a process'''


    def add_cmdline_args(self, parser):
        '''Add commandline arguments specific to this command'''
        parser.add_argument('--process', help="Name or UID of the process to start.")
        parser.add_argument('--task', help="Name or UID start task to use to begin process.  Not required if only one")
        parser.add_argument('--vars', help="Variables to set in new process.  Use format var1=val1,var2=val2")
        parser.add_argument('--draft', help="By default, new case will be routed."+
                                            "  This will not route and cause case to stay in draft",
                            action = 'store_true')


    def run(self, args):
        '''Perform command actions'''

        creds = self._load_creds(args)
        server = PMServer(creds)

        # Check args
        if args.process is None:
            raise UsageError("--process is required")

        variables = None
        if args.vars is not None:
            variables = dict()
            for pair in args.vars.split(','):
                parts = pair.split("=")
                if len(parts) != 2:
                    raise UsageError("Can't decode variable setting: " + pair)
                name, value = parts
                variables[name.strip()] = value.strip()

        # Get Process
        process = server.find_process(args.process)
        if process is None:
            raise UsageError("Can't find process: %s" % (args.process))

        # Find starting task
        task_uid = None
        if args.task is not None:
            for task in process.list_start_tasks():
                if task.name == args.task:
                    task_uid = task.uid
                elif len(args.task) >= 6:
                    if task.uid.startswith(args.task) or task.uid.endswith(args.task):
                        task_uid = task.uid
            if task_uid is None:
                raise UsageError("Can't find task '%s' in process %s" % (
                    args.task, process.name))

        # Start the process
        case = process.start(task_uid, variables, (not args.draft))

        print("Started case %s (%s)" % (case.name, case.uid))

