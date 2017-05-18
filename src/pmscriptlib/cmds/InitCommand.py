import os
from textwrap import dedent
from getpass import getpass

from .exceptions import CmdArgumentValueError
from .Command import Command
from ..Credentials import Credentials

class InitCommand(Command):
    '''Initialize a new credentials file'''

    def add_cmdline_args(self, parser):
        '''Add commandline arguments specific to this command'''
        pass


    def run(self, args):
        '''Perform command actions'''

        path = os.path.abspath(args.creds)
        if os.path.exists(path):
            raise CmdArgumentValueError('Credential file %s already exists' % (path))

        creds = Credentials()

        creds.base_url      = input("Base URL (eg: http://my_server): ").strip().rstrip('/')
        creds.workspace     = input("Name of the workspace:           ")

        print(dedent("""
            In order to use the ProcessMaker API, you'll need to register an application
            in the process maker interface.

              1) Access your ProcessMaker server
              2) Login with the user this script will connect as
                 (role needs to be MANAGER or ADMIN)
              3) Visit URL:
                 {base_url}/sys{workspace}/en/neoclassic/oauth2/applications
              4) Add a new application (none of the parameters affect this script)
              5) Record the Client ID and the Client Secret
            """).format(
                base_url = creds.base_url,
                workspace = creds.workspace))

        creds.username      = input("Username to authenticate: ")
        creds.client_id     = input("Client ID:                ")
        creds.client_secret = input("Client Secret:            ")
        creds.password      = getpass("Password (optional):      ")

        print("\nWriting", path)
        creds.save_to(path)

        print("Finished")