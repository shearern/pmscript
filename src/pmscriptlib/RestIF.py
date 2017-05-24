import os
import sys
import requests
import json

from .Cache import Cache
from .exceptions import CredentialsError, RequestError

class RestIF:
    '''Interface for making REST calls'''

    def __init__(self, creds):
        self.creds = creds

        self.cache = Cache(
            path = os.path.join(
                        os.path.dirname(creds.path),
                        '.' + os.path.basename(creds.path).lstrip('.') + '.cache'),
            expire_mins = 3 * 24 * 60
        )

        self.__trying_login = False


    def _get_new_access_token(self):

        # Assemble credentials for login
        request_data = {
            'client_id':        self.creds.client_id,
            'grant_type':       'password',
            'username':         self.creds.username,
            'password':         self.creds.password,
            'client_secret':    self.creds.client_secret,
        }

        # Perform login
        headers = {
            'Content-Type': "application/json",
        }
        url = '{base}/{workspace}/oauth2/token'.format(
            base = self.creds.base_url,
            workspace = self.creds.workspace)
        r = requests.post(url, headers=headers, data=json.dumps(request_data))

        if not r.ok:
            raise CredentialsError("Failed to login: %s" % (r.text))
        else:
            response_data = r.json()
            access_token = response_data['access_token']

        self.creds.access_token = access_token
        self.creds.save()


    def get(self, url):

        # Make sure we have an access token
        if self.creds.access_token is None:
            self._get_new_access_token()

        # Format URL
        url = url.format(
            base = self.creds.base_url,
            workspace = self.creds.workspace)
        headers = {
            'Authorization': 'Bearer ' + self.creds.access_token,
        }

        # Make Request
        r = requests.get(url, headers=headers)

        # Check response
        if not r.ok:

            # Retrieve error message
            try:
                response_data = r.json()
            except:
                response_data = "Text: " + r.text()

            # Check for expired access token
            try:
                if response_data['error']['message'] == "Unauthorized":
                    # Already tried to relogin?
                    if self.__trying_login:
                        raise CredentialsError("Unauthorized to access %s" % (url))
                    # Try to login
                    else:
                        print("Access token has expired.  Requesting new one.", file=sys.stderr)
                        self.__trying_login = True
                        self._get_new_access_token()
                        rtn = self.get(url)
                        self.__trying_login = False
                        return rtn
            except:
                pass

            # Check for an error message
            try:
                raise RequestError("Got error %s while accessing %s" % (response_data['error']['message'], url))
            except:
                raise RequestError("Got responce %s while accessing %s" % (response_data, url))


        # Decode response
        else:
            try:
                return r.json()
            except:
                raise RequestError("Response to %s is not json: %s" % (
                    url, r.text()))



