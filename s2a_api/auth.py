import logging
import json
import requests
import exception
from error_handler import hadle_error

LOG = logging.getLogger(__name__)

class AuthService(object):
    
    def __init__(self, api_url, client_id, client_secret):
        self.api_url = api_url
        self.client_id = client_id
        self.client_secret = client_secret
    
    def get_token(self, code):
        """ Get token """
        LOG.info("Calling authentication service")
        
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        
        data = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code
            }
            
        resp = requests.post(url=self.api_url, data=data, headers=headers, verify=False)
        
        if resp.status_code == 200:
            try:
                json_dict = resp.json()
                LOG.info("Response code = " + str(resp.status_code))
                if json_dict.has_key('access_token'):
                    return str(json_dict.get('access_token'))
                else:
                    raise KeyError("Response is missing access_token")
            except:
                LOG.exception("API returned corrupted message")
                raise
        else:
            handle_error(resp)
        
        
       
