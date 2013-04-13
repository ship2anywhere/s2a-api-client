import logging
import json
import requests
import exception
from error_handler import handle_error

LOG = logging.getLogger(__name__)

class TrackService(object):
  
    def __init__(self, api_url):
        self.api_url = api_url

    def track(self, id):
        """ Track """
        LOG.info("Calling track service")
        url = self.api_url + id
        resp = requests.get(url=url, verify=False)

        if resp.status_code == requests.codes['OK']:
            #assert resp.status_code == resp.json().get('code'), "Return Codes do not match."
            try:
                json_dict = resp.json()
                LOG.info("Response code = " + str(resp.status_code))
                return json_dict
            except ValueError:
                LOG.exception("API returned corrupted message")
                raise
        
        else:
            handle_error(resp)
