
from .RestObject import RestObject
from .Project import Project
from .Case import Case
from .RestIF import RestIF

class PMServer:
    '''Access the root level of the PM Server'''

    def __init__(self, creds):
        self.__if = RestIF(creds)


    def list_projects(self):
        '''Get a list of projects'''
        return Project.list_projects(self.__if)


    def list_cases(self):
        return Case.list_cases(self.__if)

