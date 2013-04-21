import logging
from util import append_slash
from util import api_call

LOG = logging.getLogger(__name__)

class AuthService(object):
    
    def __init__(self, api_url, client_id, client_secret, verify_cert=False):
        self.api_url = append_slash(api_url)
        self.client_id = client_id
        self.client_secret = client_secret
        self.verify_cert = verify_cert
    
    def get_token(self, code):
        """ Get token """
        
        url = self.api_url + 'access_token/'
        
        headers = {'Accept': 'text/plain'}
        data = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code
            }
        
        return api_call("post", url, data=data, headers=headers,
            verify_cert=self.verify_cert)
