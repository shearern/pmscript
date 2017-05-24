import requests

from .RestObject import RestObject
from .exceptions import RestAttributeMissing

class Task(RestObject):
    '''
    A running process instance

    LIST_LVL: GET /api/1.0/{workspace}/cases/{app_uid}/tasks
       {
          "tas_uid":         "64109086255b6822b4aaa00042124344",
          "tas_title":       "Register Client",
          "tas_description": "Task to register a new client",
          "tas_start":       1,
          "tas_type":        "NORMAL",
          "tas_derivation":  "NORMAL",
          "tas_assign_type": "BALANCED",
          "usr_uid":         "24175319155b67db9cb2b77069631302",
          "usr_username":    "wendy",
          "usr_firstname":   "Wendy",
          "usr_lastname":    "Smith",
          "route":
          {
             "type":         "PARALLEL",
             "to":
             [
                {
                   "rou_number":    1,
                   "rou_condition": "",
                   "tas_uid":       "71294923755b67a04a06590067310340",
                },
                {
                   "rou_number":    2,
                   "rou_condition": "",
                   "tas_uid":       "81106116155b679c396cd47013780044",
                }
             ]
          },
          "delegations":
          [
             {
                "del_index":         1,
                "del_init_date":     "2015-07-27 15:15:39",
                "del_task_due_date": "2015-07-28 15:15:39",
                "del_finish_date":   "2015-07-27 15:16:16",
                "del_duration":      "0 Hours 0 Minutes 37 Seconds",
                "usr_uid":           "24175319155b67db9cb2b77069631302",
                "usr_username":      "wendy",
                "usr_firstname":     "Wendy",
                "usr_lastname":      "Smith",
             }
          ],
          "status":          "TASK_COMPLETED"
       },

    '''


    def __init__(self, rif, case_uid, uid, data=None, data_level=1):
        if data_level > self.LIST_LVL:
            raise Exception("I don't think you can get task detail...")
        self.__case_uid = case_uid
        super(Task, self).__init__(rif, uid, data, data_level)


    @property
    def _uid_key(self):
        return 'tas_uid'


    @property
    def case_uid(self):
        return self.__case_uid


    @property
    def case(self):
        return self._assoc_rest_obj('Case', self.case_uid)


    @property
    def process_uid(self):
        return self._rest_obj_attr(self.LIST_LVL, 'pro_uid')


    @property
    def process(self):
        return self._assoc_rest_obj('Process', self.process_uid)


    @property
    def name(self):
        try:
            return self._rest_obj_attr(self.LIST_LVL, 'tas_title')
        except RestAttributeMissing:
            return "Unknown"


    def __str__(self):
        return self.name


    def __repr__(self):
        return 'Task(case_uid="%s", uid="%s")' % (self.case_uid, self.uid)


    @property
    def type(self):
        return self._rest_obj_attr(self.LIST_LVL, 'tas_type')


    @property
    def description(self):
        return self._rest_obj_attr(self.LIST_LVL, 'tas_description')


    @property
    def username(self):
        return self._rest_obj_attr(self.LIST_LVL, 'usr_username')


    @property
    def started(self):
        try:
            return int(self._rest_obj_attr(self.LIST_LVL, 'tas_start')) == 1
        except:
            return False


    @property
    def status(self):
        return self._rest_obj_attr(self.LIST_LVL, 'status')


    def _retireve_obj_detail(self):
        raise NotImplementedError("API doesn't have a get task detail endpoint (I don't think)")


    @staticmethod
    def list_tasks_for_case(rif, case_uid):
        for data in rif.get('{base}/api/1.0/{workspace}/cases/%s/tasks' % (case_uid)):
            yield Task(rif, case_uid, data['tas_uid'], data=data, data_level=Task.LIST_LVL)


