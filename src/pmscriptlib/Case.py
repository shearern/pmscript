import requests

from .RestObject import RestObject
from .exceptions import RequestError

class Case(RestObject):
    '''
    A running process instance

    LIST_LVL:
       {
          "app_uid":"561670297591cae63767764067301702",
          "del_index":"2",
          "del_last_index":"1",
          "app_number":"2",
          "app_status":"TO_DO",
          "usr_uid":"823570034591c9ccb563c67040305429",
          "previous_usr_uid":"823570034591c9ccb563c67040305429",
          "tas_uid":"18946129658ed6284a64304054009168",
          "pro_uid":"28738129658ed550c14df31067804511",
          "del_delegate_date":"2017-05-17 13:12:39",
          "del_init_date":null,
          "del_finish_date":null,
          "del_task_due_date":"2017-05-18 13:12:39",
          "del_risk_date":"2017-05-18 11:36:39",
          "del_thread_status":"OPEN",
          "app_thread_status":"OPEN",
          "app_title":"#2",
          "app_pro_title":"Recording Processing",
          "app_tas_title":"Create Website Record",
          "app_current_user":"Script Python",
          "app_del_previous_user":"Script Python",
          "del_priority":"NORMAL",
          "del_duration":"0",
          "del_queue_duration":"0",
          "del_delay_duration":"0",
          "del_started":"0",
          "del_finished":"0",
          "del_delayed":"0",
          "app_create_date":"2017-05-17 13:11:15",
          "app_finish_date":null,
          "app_update_date":"2017-05-17 13:12:39",
          "app_overdue_percentage":"0",
          "usr_firstname":"Python",
          "usr_lastname":"Script",
          "usr_username":"pyscript",
          "appdelcr_app_tas_title":"Create Website Record",
          "usrcr_usr_uid":"823570034591c9ccb563c67040305429",
          "usrcr_usr_firstname":"Python",
          "usrcr_usr_lastname":"Script",
          "usrcr_usr_username":"pyscript",
          "previous_usr_firstname":"Python",
          "previous_usr_lastname":"Script",
          "previous_usr_username":"pyscript",
          "app_status_label":"To do"
       }

    DETAIL_LVL:
        {
           "app_uid": "36722263554ca70b82c52e8020802754",
           "app_number": "5",
           "app_name": "#5",
           "app_status": "TO_DO",
           "app_init_usr_uid": "00000000000000000000000000000001",
           "app_init_usr_username": "Administrator",
           "pro_uid": "35648267754ca36d119ecc1014698225",
           "pro_name": "Safety training course",
           "app_create_date": "2015-01-29 12:41:12",
           "app_update_date": "2015-01-29 13:21:55",
           "current_task":
              (
                 {
                    "usr_uid": "00000000000000000000000000000001",
                    "usr_name": "Administrator",
                    "tas_uid": "89626647354ca3c43743e66000804527",
                    "tas_title": "Written safety test",
                    "del_index":  2,
                    "del_thread": 2,
                    "del_thread_status": "OPEN"
                 },
                 {
                    "usr_uid": "00000000000000000000000000000001",
                    "usr_name": "Administrator",
                    "tas_uid": "60687790754ca3c434b57d5092245736",
                    "tas_title": "Practice safety with trainer",
                    "del_index": 3,
                    "del_thread": 3,
                    "del_thread_status": "OPEN"
                 }
              )
        }

    '''


    @property
    def _uid_key(self):
        return 'app_uid'


    @property
    def title(self):
        return self._rest_obj_attr(self.LIST_LVL, 'app_title')


    @property
    def process_uid(self):
        '''UID of the process this case is an instance of'''
        return self._rest_obj_attr(self.LIST_LVL, 'pro_uid')


    @property
    def process(self):
        '''Process object this case is an instance of'''
        return self._assoc_rest_obj('Project', self.process_uid)



    @staticmethod
    def list_cases(rif):
        for data in rif.get('{base}/api/1.0/{workspace}/cases'):
            yield Case(rif, data['app_uid'], data=data, data_level=Case.LIST_LVL)


