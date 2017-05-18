import string

from abc import ABCMeta, abstractmethod, abstractproperty

from ..Credentials import Credentials

def calc_command_name_from_class_name(class_name):

    if class_name.endswith("Command"):
        class_name = class_name[:-1*len("Command")]

    name = ''
    for c in class_name:
        if c in string.ascii_uppercase:
            name += '_' + c.lower()
        else:
            name += c
    return name.lstrip('_')


class Command(metaclass=ABCMeta):
    '''Base class for implementing commands in pmscript'''

    @property
    def cmd_name(self):
        '''Return name to invoke this command'''
        return calc_command_name_from_class_name(self.__class__.__name__)


    @property
    def cmd_help(self):
        '''Describe how to use this command'''
        return self.__doc__


    @abstractmethod
    def add_cmdline_args(self, parser):
        '''Add commandline arguments specific to this command'''


    @abstractmethod
    def run(self, args):
        '''Perform command actions'''


    def _load_creds(self, args):
        creds = Credentials(args.creds)
        creds.load()
        return creds