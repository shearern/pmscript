
from .RestObject import RestObject
from .Project import Project

class PMServer(RestObject):
    '''Access the root level of the PM Server'''

    def list_projects(self):
        '''Get a list of projects'''
        return Project.list_projects(self.creds)

