import requests

from .RestObject import RestObject
from .exceptions import RequestError

class Project(RestObject):
    '''
    A project on the server (process / workflow)

    LIST_LVL:
        {
            "prj_uid":"28738129658ed550c14df31067804511",
            "prj_name":"Recording Processing",
            "prj_description":"",
            "prj_category":"",
            "prj_type":"bpmn",
            "prj_create_date":"2017-04-11 15:13:32",
            "prj_update_date":"2017-05-17 11:49:23",
            "prj_status":"ACTIVE"
        }

    DETAIL_LVL:
        {
          "prj_uid": "28738129658ed550c14df31067804511",
          "prj_name": "Recording Processing",
          "prj_description": "",
          "prj_target_namespace": null,
          "prj_expresion_language": null,
          "prj_type_language": null,
          "prj_exporter": null,
          "prj_exporter_version": null,
          "prj_create_date": "2017-04-11 15:13:32",
          "prj_update_date": "2017-05-17 13:08:32",
          "prj_author": "00000000000000000000000000000001",
          "prj_author_version": null,
          "prj_original_source": null,
          "diagrams": [
            {
              "dia_uid": "59395493158ed550c2d5261053623334",
              "prj_uid": "28738129658ed550c14df31067804511",
              "dia_name": "Recording Processing",
              "dia_is_closable": 0,
              "pro_uid": "21870325558ed550c3ee174075403352",
              "activities": [
                {
                  "act_uid": "18946129658ed6284a64304054009168",
                  "act_name": "Create Website Record",
                  "act_type": "TASK",
                  "act_is_for_compensation": "0",
                  "act_start_quantity": "1",
                  "act_completion_quantity": "0",
                  "act_task_type": "USERTASK",
                  "act_implementation": "",
                  "act_instantiate": "0",
                  "act_script_type": "",
                  "act_script": "",
                  "act_loop_type": "EMPTY",
                  "act_test_before": "0",
                  "act_loop_maximum": "0",
                  "act_loop_condition": "0",
                  "act_loop_cardinality": "0",
                  "act_loop_behavior": "0",
                  "act_is_adhoc": "0",
                  "act_is_collapsed": "0",
                  "act_completion_condition": "0",
                  "act_ordering": "0",
                  "act_cancel_remaining_instances": "0",
                  "act_protocol": "0",
                  "act_method": "0",
                  "act_is_global": "0",
                  "act_referer": "0",
                  "act_default_flow": "0",
                  "act_master_diagram": "0",
                  "bou_element": "767786928591cadb50cafa7016766972",
                  "bou_x": "534",
                  "bou_y": "301",
                  "bou_width": "192",
                  "bou_height": "41",
                  "bou_container": "bpmnDiagram"
                },
                {
                  "act_uid": "17339379458ed56f4a76895075742354",
                  "act_name": "New Recording",
                  "act_type": "TASK",
                  "act_is_for_compensation": "0",
                  "act_start_quantity": "1",
                  "act_completion_quantity": "0",
                  "act_task_type": "USERTASK",
                  "act_implementation": "",
                  "act_instantiate": "0",
                  "act_script_type": "",
                  "act_script": "",
                  "act_loop_type": "EMPTY",
                  "act_test_before": "0",
                  "act_loop_maximum": "0",
                  "act_loop_condition": "0",
                  "act_loop_cardinality": "0",
                  "act_loop_behavior": "0",
                  "act_is_adhoc": "0",
                  "act_is_collapsed": "0",
                  "act_completion_condition": "0",
                  "act_ordering": "0",
                  "act_cancel_remaining_instances": "0",
                  "act_protocol": "0",
                  "act_method": "0",
                  "act_is_global": "0",
                  "act_referer": "0",
                  "act_default_flow": "0",
                  "act_master_diagram": "0",
                  "bou_element": "767786928591cadb50cafa7016766972",
                  "bou_x": "163",
                  "bou_y": "57",
                  "bou_width": "151",
                  "bou_height": "42",
                  "bou_container": "bpmnDiagram"
                }
              ],
              "events": [
                {
                  "evn_uid": "52101655958ed571ce1e5b6027019289",
                  "evn_name": "",
                  "evn_type": "START",
                  "evn_marker": "EMPTY",
                  "evn_is_interrupting": "1",
                  "evn_cancel_activity": "0",
                  "evn_activity_ref": null,
                  "evn_wait_for_completion": "0",
                  "evn_error_name": null,
                  "evn_error_code": null,
                  "evn_escalation_name": null,
                  "evn_escalation_code": null,
                  "evn_message": "LEAD",
                  "evn_operation_name": null,
                  "evn_operation_implementation_ref": null,
                  "evn_time_date": null,
                  "evn_time_cycle": null,
                  "evn_time_duration": null,
                  "evn_behavior": "CATCH",
                  "bou_element": "767786928591cadb50cafa7016766972",
                  "bou_x": "57",
                  "bou_y": "62",
                  "bou_width": "33",
                  "bou_height": "33",
                  "bou_container": "bpmnDiagram"
                },
                {
                  "evn_uid": "93648257158ed6284bfe8f1083914444",
                  "evn_name": "",
                  "evn_type": "END",
                  "evn_marker": "EMPTY",
                  "evn_is_interrupting": "1",
                  "evn_cancel_activity": "0",
                  "evn_activity_ref": null,
                  "evn_wait_for_completion": "0",
                  "evn_error_name": null,
                  "evn_error_code": null,
                  "evn_escalation_name": null,
                  "evn_escalation_code": null,
                  "evn_message": "",
                  "evn_operation_name": null,
                  "evn_operation_implementation_ref": null,
                  "evn_time_date": null,
                  "evn_time_cycle": null,
                  "evn_time_duration": null,
                  "evn_behavior": "THROW",
                  "bou_element": "767786928591cadb50cafa7016766972",
                  "bou_x": "895",
                  "bou_y": "305",
                  "bou_width": "33",
                  "bou_height": "33",
                  "bou_container": "bpmnDiagram"
                }
              ],
              "gateways": [],
              "flows": [
                {
                  "flo_uid": "48148888158ed6284c55924074523217",
                  "flo_type": "SEQUENCE",
                  "flo_name": " ",
                  "flo_element_origin": "18946129658ed6284a64304054009168",
                  "flo_element_origin_type": "bpmnActivity",
                  "flo_element_dest": "93648257158ed6284bfe8f1083914444",
                  "flo_element_dest_type": "bpmnEvent",
                  "flo_is_inmediate": "1",
                  "flo_condition": null,
                  "flo_x1": "727",
                  "flo_y1": "322",
                  "flo_x2": "895",
                  "flo_y2": "322",
                  "flo_state": [
                    {
                      "x": 727,
                      "y": 322
                    },
                    {
                      "x": 895,
                      "y": 322
                    }
                  ],
                  "flo_position": "1"
                },
                {
                  "flo_uid": "91751875058ed571d005234056481909",
                  "flo_type": "SEQUENCE",
                  "flo_name": " ",
                  "flo_element_origin": "52101655958ed571ce1e5b6027019289",
                  "flo_element_origin_type": "bpmnEvent",
                  "flo_element_dest": "17339379458ed56f4a76895075742354",
                  "flo_element_dest_type": "bpmnActivity",
                  "flo_is_inmediate": "1",
                  "flo_condition": null,
                  "flo_x1": "90",
                  "flo_y1": "79",
                  "flo_x2": "163",
                  "flo_y2": "79",
                  "flo_state": [
                    {
                      "x": 90,
                      "y": 79
                    },
                    {
                      "x": 163,
                      "y": 79
                    }
                  ],
                  "flo_position": "1"
                },
                {
                  "flo_uid": "96024847458ed6284c54278086923524",
                  "flo_type": "SEQUENCE",
                  "flo_name": " ",
                  "flo_element_origin": "17339379458ed56f4a76895075742354",
                  "flo_element_origin_type": "bpmnActivity",
                  "flo_element_dest": "18946129658ed6284a64304054009168",
                  "flo_element_dest_type": "bpmnActivity",
                  "flo_is_inmediate": "1",
                  "flo_condition": null,
                  "flo_x1": "314",
                  "flo_y1": "79",
                  "flo_x2": "534",
                  "flo_y2": "322",
                  "flo_state": [
                    {
                      "x": 314,
                      "y": 79
                    },
                    {
                      "x": 424,
                      "y": 79
                    },
                    {
                      "x": 424,
                      "y": 322
                    },
                    {
                      "x": 534,
                      "y": 322
                    }
                  ],
                  "flo_position": "1"
                }
              ],
              "artifacts": [],
              "laneset": [],
              "lanes": [],
              "data": [],
              "participants": []
            }
          ]
        }

    '''

    LIST_LVL=1
    DETAIL_LVL=2

    def __init__(self, creds, prj_uid, data=None, data_level=None):
        super(Project, self).__init__(creds)
        self.__uid = prj_uid
        self.__data = data
        self.__data_level = data_level


    def _retrieve_detail(self):
        # Retrieve project details
        url = '{base}/api/1.0/{workspace}/project/{uid}'.format(
            base = self.creds.base_url,
            workspace = self.creds.workspace,
            uid = self.__uid)
        headers = {
            'Authorization': 'Bearer ' + self.creds.access_token,
        }
        r = requests.get(url)
        if not r.ok:
            raise RequestError("Failed to retrieve project %s details: %s" % (
                self.__uid, r.text))

        self.__data = r.json()
        self.__data_level = self.DETAIL_LVL

        try:
            assert(self.__data['prj_uid'] == self.__uid)
        except:
            raise RequestError("Requested project %s, but got %s" % (self.__uid, self.__data))


    def _get_rest_data(self, level, key):
        if self.__data is None or self.__data_level is None or self.__data_level < level:
            self._retrieve_detail()
        return self.__data[key]


    @property
    def name(self):
        return self._get_rest_data(self.LIST_LVL, 'prj_name')

    @property
    def uid(self):
        return self.__uid


    def __str__(self):
        return self.name


    def __repr__(self):
        return 'Project(prj_uid="%s")' % (self.uid)



    @staticmethod
    def list_projects(creds):
        url = '{base}/api/1.0/{workspace}/project'.format(
            base = creds.base_url,
            workspace = creds.workspace)
        headers = {
            'Authorization': 'Bearer ' + creds.access_token,
        }
        r = requests.get(url, headers=headers)
        if not r.ok:
            raise RequestError("Failed to list projects: %s" % (r.text))

        for data in r.json():
            yield Project(creds, data['prj_uid'], data=data, data_level=Project.LIST_LVL)
