'''pmscript.py - Script for interacting with a ProcessMaker server'''
import os
import sys

import argparse
import requests
import tabulate

from pmscriptlib import CredentialsError, RequestError
from pmscriptlib.cmds import ALL_CMDS, UsageError


def arg_parser():
    parser = argparse.ArgumentParser(description="Script for interacting with a ProcessMaker server")
    parser.add_argument('--creds', help="Path to credentials file to access the server")
    subparsers = parser.add_subparsers(
        title = 'commands',
        description = 'valid commands',
        dest = 'command',
    )

    # Add parsers for sub commands
    for cmd in sorted(ALL_CMDS.values(), key=lambda c: c.cmd_name):
        sub_parser = subparsers.add_parser(cmd.cmd_name, help=cmd.cmd_help)
        cmd.add_cmdline_args(sub_parser)

    return parser


if __name__ == '__main__':

    # Parse Args
    parser = arg_parser()
    args = parser.parse_args()

    # Run command
    try:
        ALL_CMDS[args.command].run(args)
    except UsageError as e:
        print("Usage Error: " + str(e))
        parser.print_usage()
        sys.exit(1)
    except CredentialsError as e:
        print("AUTH ERROR:", str(e))
        sys.exit(1)
    except RequestError as e:
        print("Error encountered in API request:\n%s" % (str(e)))

