import logging
import json
from util import append_slash
from util import api_call

LOG = logging.getLogger(__name__)

class QuoteService(object):
  
    def __init__(self, api_url, verify_cert = False):
        self.api_url = append_slash(api_url)
        self.verify_cert = verify_cert

    def get_quote(self, request):
        """ Get quote """
        req = {"request": request}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        
        return api_call("post", self.api_url, data=json.dumps(req), headers=headers)
