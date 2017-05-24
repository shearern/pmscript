'''Create a new command class'''
import os
import sys

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
    path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                           'pmscriptlib', 'cmds', '__init__.py'))
    print("Add to ALL_CMDS in %s:" % (path))
    print("  from .%s import %s" % (class_name, class_name))
    print("  %s()," % (class_name))
