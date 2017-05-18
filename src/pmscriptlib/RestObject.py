
from abc import ABCMeta, abstractmethod, abstractproperty

class RestObject(metaclass=ABCMeta):
    '''Base object for access the ProcessMaker API'''

    def __init__(self, creds):
        self.creds = creds


