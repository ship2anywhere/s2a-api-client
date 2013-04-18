import logging
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
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'} # url-encoded
        data = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code
            }
        
        return api_call("post", self.api_url, data=data, headers=headers,
            verify_cert=self.verify_cert)
