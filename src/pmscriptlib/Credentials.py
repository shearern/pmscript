import os
import json
from getpass import getpass
import requests

from .exceptions import CredentialsError

class Credentials(object):
    '''Credentials stores data about how to access the API'''

    def __init__(self, path):
        self.__path = path

        self.base_url = None
        self.workspace = None
        self.client_id = None
        self.client_secret = None
        self.username = None
        self.__stored_password = None
        self.__asked_password = None
        self.__access_token = None


    @property
    def path(self):
        return self.__path


    def save(self):
        with open(self.__path, 'w') as fh:
            json.dump({
                    'base_url': self.base_url,
                    'workspace': self.workspace,
                    'client_id': self.client_id,
                    'client_secret': self.client_secret,
                    'username': self.username,
                    'password': self.__stored_password,
                    'access_token': self.__access_token,
                },
                fp=fh,
                sort_keys=True,
                indent=4,
                separators=(',', ': '))

    def load(self):
        try:
            with open(self.__path, 'r') as fh:
                data = json.load(fh)
        except Exception as e:
            raise CredentialsError("Failed to read credential file %s: %s" % (
                os.path.abspath(self.__path),
                str(e)))

        def _get_required(name):
            try:
                return data[name]
            except:
                raise CredentialsError("Required data %s is missing from %s" % (
                    name, os.path.abspath(self.__path)))

        def _get_optional(name):
            try:
                return data[name]
            except:
                return None

        self.base_url = _get_required('base_url')
        self.workspace = _get_required('workspace')
        self.client_id = _get_required('client_id')
        self.client_secret = _get_required('client_secret')
        self.username = _get_required('username')
        self.__stored_password = _get_optional('password')
        self.__access_token = _get_optional('access_token')


    @property
    def password(self):
        if self.__stored_password is None or len(self.__stored_password) == 0:
            if self.__asked_password is None:
                self.__asked_password = getpass("Password to connect as %s: " % (self.username))
            return self.__asked_password
        else:
            return self.__stored_password
    @password.setter
    def password(self, value):
        self.__stored_password = value


    @property
    def access_token(self):
        '''Cache access token in creds file to speed up repeat command calls'''

        if self.__access_token is None:

            # Assemble credentials for login
            request_data = {
                'client_id':        self.client_id,
                'grant_type':       'password',
                'username':         self.username,
                'password':         self.password,
                'client_secret':    self.client_secret,
            }

            # Perform login
            headers = {
                'Content-Type': "application/json",
            }
            url = '{base}/{workspace}/oauth2/token'.format(
                base = self.base_url,
                workspace = self.workspace)
            r = requests.post(url, headers=headers, data=json.dumps(request_data))

            if not r.ok:
                raise CredentialsError("Failed to login: %s" % (r.text))
            else:
                response_data = r.json()
                self.__access_token = response_data['access_token']

                self.save()

        return self.__access_token
