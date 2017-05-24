'''Create a new command class'''
import os
import sys
from textwrap import dedent

if __name__ == '__main__':

    cmd = input("Name of command (e.g. list_projects): ")

    next_is_upper = True
    class_name = ''
    for c in cmd:
        if c == '_':
            next_is_upper = True
        else:
            if next_is_upper:
                class_name += c.upper()
                next_is_upper = False
            else:
                class_name += c
    class_name += 'Command'

    path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                           'pmscriptlib', 'cmds', class_name + '.py'))

    if os.path.exists(path):
        print("ERROR: %s already exists" % (class_name))
        sys.exit(2)

    help = input("Description: ")

    print("Writing", path)
    with open(path, "w") as fh:
        fh.write("""\

from .Command import Command

class {class_name}(Command):
    '''{help}'''


    def add_cmdline_args(self, parser):
        '''Add commandline arguments specific to this command'''
        # parser.add_argument('--process', help="Name or UID of the process to list cases for.")


    def run(self, args):
        '''Perform command actions'''
        raise NotImplementedError()

    """.format(
            class_name = class_name,
            help = help))

    print("")

    # === Add class to __init__.py ===
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                           'pmscriptlib', 'cmds', '__init__.py'))
    with open(path, 'r') as fh:
        src = [line.rstrip() for line in fh.readlines()]

    # Import
    token = '# Import CMDs here'
    try:
        src.insert(src.index(token)+1, 'from .{class_name) import {class_name}'.format(class_name=class_name))
    except ValueError:
        print("ERROR: Failed to find token: " + token)

    # Add to list of classes
    token = '    # Add CMD class here'
    try:
        src.insert(src.index(token)+1, '    {class_name}(),'.format(class_name=class_name))
    except ValueError:
        print("ERROR: Failed to find token: " + token)

    with open(path, 'w') as fh:
        fh.write("\n".join(src))

