import logging
import json
import requests
import exception
from error_handler import hadle_error

LOG = logging.getLogger(__name__)

class OrderService(object):
  
    def __init__(self, api_url):
        self.api_url = api_url

    def make_order(self, request, token):
        """ Get order """
        LOG.info("Calling quote service")
        req = {"request": request}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        resp = requests.post(url=self.api_url, data=json.dumps(req), headers=headers, verify=False)

        if resp.status_code == requests.codes['OK']:
            #assert resp.status_code == resp.json().get('code'), "Return Codes do not match."
            try:
                json_dict = resp.json()
                LOG.info("Response code = " + str(resp.status_code))
                return json_dict
            except ValueError:
                msg = "API returned corrupted message"
                LOG.exception(msg)
                return msg
        
        else:
            handle_error(resp)
