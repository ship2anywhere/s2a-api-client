import logging
import json
import requests
import exception
from error_handler import handle_error
from util import append_slash

LOG = logging.getLogger(__name__)

class QuoteService(object):
  
    def __init__(self, api_url, verify_cert = False):
        self.api_url = append_slash(api_url)
        self.verify_cert = verify_cert

    def get_quote(self, request):
        """ Get quote """
        req = {"request": request}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        
        if LOG.isEnabledFor(logging.DEBUG):
            LOG.debug("Request URL: %s ; Request Data: %s" % (self.api_url, req))
        
        resp = requests.post(url=self.api_url, data=json.dumps(req), headers=headers, verify = verify_cert)

        if LOG.isEnabledFor(logging.DEBUG):
            LOG.debug("Status Code: %s; Response Body: %s" % (resp.status_code, resp.text))
        
        handle_error(resp)

        try:
            json_dict = resp.json()
            return json_dict
        except ValueError:
            LOG.exception("API returned corrupted message")
            raise S2aApiException("API returned corrupted message: " + str(e))

