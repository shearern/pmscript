import requests

from .exceptions import RequestError

from .RestObject import RestObject
from .StartingTask import StartingTask
from .Case import Case

class Process(RestObject):
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


    @property
    def _uid_key(self):
        return 'prj_uid'


    def _detail_url(self):
        return '{base}/api/1.0/{workspace}/project/%s' % (self.uid)

    @property
    def name(self):
        return self._rest_obj_attr(self.LIST_LVL, 'prj_name')

    @property
    def description(self):
        return self._rest_obj_attr(self.LIST_LVL, 'prj_description')

    @property
    def category(self):
        return self._rest_obj_attr(self.LIST_LVL, 'prj_category')

    @property
    def status(self):
        return self._rest_obj_attr(self.LIST_LVL, 'prj_status')


    def __str__(self):
        return self.name


    def __repr__(self):
        return 'Process(uid="%s")' % (self.uid)


    def list_start_tasks(self):
        return StartingTask.list_start_tasks_for_process(self.rif, self.uid)



    @staticmethod
    def list_processes(rif):
        for data in rif.get('{base}/api/1.0/{workspace}/project'):
            yield Process(rif, data['prj_uid'], data=data, data_level=Process.LIST_LVL)



    def start(self, start_task_uid=None, variables=None, route=True):
        '''
        Start a new process (create a case)

        :param variables: Dictionary of variables to set on the new case
        :param start_task_uid:
            Which of the entry points (starting tasks) to use to start the process
            If not speicified, then defaults if only one start task is available
        :param route:
            If false, then case begins in a draft state
            If true, call .route() on case to move out of draft status
        :return: Case
        '''

        # Determine start_task_uid
        if start_task_uid is None:
            for start_task in self.list_start_tasks():
                if start_task_uid is not None:
                    raise RequestError(
                        "Multiple start tasks exists for %s.  Must specify which to use" % (
                            self.name))
                else:
                    start_task_uid = start_task.uid

        # Create case
        case = Case.create(self.rif, self.uid, start_task_uid, variables)

        # Route to go to next task in process
        if route:
            case.route()

        return case

