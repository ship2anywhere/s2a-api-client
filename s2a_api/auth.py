import logging
import json
import requests
import exception
from error_handler import hadle_error

LOG = logging.getLogger(__name__)

class AuthService(object):
    
    def __init__(self, api_url, client_id, client_secret, verify_cert=False):
        self.api_url = api_url
        self.client_id = client_id
        self.client_secret = client_secret
        self.verify_cert = verify_cert
    
    def get_token(self, code):
        """ Get token """        
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        data = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code
            }
        
        if LOG.isEnabledFor(logging.DEBUG):
            LOG.debug("Request URL: %s" % (url,))
            
        resp = requests.post(url=self.api_url, data=data, headers=headers, verify=self.verify_cert)
         
        if LOG.isEnabledFor(logging.DEBUG):
            LOG.debug("Status Code: %s; Response Body: %s" % (resp.status_code, resp.text))

        handle_error(resp)
         
        try:
            json_dict = resp.json()
            if json_dict.has_key('access_token'):
                return str(json_dict.get('access_token'))
            else:
                raise KeyError("Response is missing access_token")
        except ValueError as e:
            LOG.exception("API returned corrupted message")
            raise exception.S2aApiException("API returned corrupted message: " + str(e))
        
        
       
