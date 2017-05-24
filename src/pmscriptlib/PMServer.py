
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


    def find_case(self, name, process=None):
        '''
        Find a case by it's name or UID

        :param name:
            Either all or part of the uid (begin or end), or the name of the case
            If UID, then must be at least 6 characters
        :param process:
            Either all or part of the uid or the name of the process.
            If not none, then the case must belong to the given case
        '''

        found = None

        def _matches_process(c):
            if process is None:
                return True
            if c.process.name == process:
                return True
            if len(c.process.uid) >= 6:
                if c.process.uid.startswith(process) or c.process.uid.endswith(process):
                    return True
            return False

        # Is case UID cached
        hit = False
        cache_key = 'Case.UID.search.%s.%s' % (str(process), name)
        if self.__if.cache.has(cache_key):
            cached_case = Case(self.__if, uid=self.__if.cache[cache_key]) # TODO: Need to check if uid is deleted?
            if _matches_process(cached_case):
                found = cached_case
                hit = True

        # List cases
        if found is None:
            for case in self.list_cases():
                if case.name == name:
                    if _matches_process(case):
                        found = case
                elif len(name) >= 6:
                    if case.uid.startswith(name) or case.uid.endswith(name):
                        if _matches_process(case):
                            found = case

        # Cache results
        if found is not None:
            if not hit:
                self.__if.cache[cache_key] = case.uid

        return found


