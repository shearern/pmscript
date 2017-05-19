
from .RestObject import RestObject
from .Process import Process
from .Case import Case
from .RestIF import RestIF

class PMServer:
    '''Access the root level of the PM Server'''

    def __init__(self, creds):
        self.__if = RestIF(creds)


    def list_processes(self):
        '''Get a list of projects'''
        return Process.list_processes(self.__if)


    def list_cases(self):
        return Case.list_cases(self.__if)

