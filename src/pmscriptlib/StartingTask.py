import requests

from .RestObject import RestObject
from .exceptions import RestAttributeMissing

class StartingTask(RestObject):
    '''
    A task that can be used to start a process (create a case)

    LIST_LVL: GET /api/1.0/{workspace}/project/{prj_uid}/starting-tasks
       {
          "act_name": "Engineering Request",
          "act_uid": "7845618785751f9cc81ed78079255303"
       },

    '''


    def __init__(self, rif, process_uid, uid, data=None, data_level=1):
        if data_level > self.LIST_LVL:
            raise Exception("I don't think you can get additional detail...")
        self.__process_uid = process_uid
        super(StartingTask, self).__init__(rif, uid, data, data_level)


    @property
    def _uid_key(self):
        return 'act_uid'


    @property
    def process_uid(self):
        return self.__process_uid


    @property
    def process(self):
        return self._assoc_rest_obj('Process', self.process_uid)


    @property
    def name(self):
        return self._rest_obj_attr(self.LIST_LVL, 'act_name')


    def __str__(self):
        return self.name


    def __repr__(self):
        return 'Task(case_uid="%s", uid="%s")' % (self.case_uid, self.uid)


    def _retireve_obj_detail(self):
        raise NotImplementedError("API doesn't have a get task detail endpoint (I don't think)")


    @staticmethod
    def list_start_tasks_for_process(rif, uid):
        for data in rif.get('{base}/api/1.0/{workspace}/project/%s/starting-tasks' % (uid)):
            yield StartingTask(rif, process_uid=uid, uid=data['act_uid'], data=data, data_level=RestObject.LIST_LVL)



