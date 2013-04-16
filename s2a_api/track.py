import logging
import json
import requests
import exception
from error_handler import handle_error
from util import append_slash

LOG = logging.getLogger(__name__)

class TrackService(object):
  
    def __init__(self, api_url, verify_cert = False):
        self.api_url = append_slash(api_url)
        self.verify_cert = verify_cert

    def track(self, tracking_number):
        """ Track """
        url = self.api_url + tracking_number + "/"
        
        if LOG.isEnabledFor(logging.DEBUG):
            LOG.debug("Request URL: %s" % (url,))
        
        resp = requests.get(url=url, verify=self.verify_cert)
        
        if LOG.isEnabledFor(logging.DEBUG):
            LOG.debug("Status Code: %s; Response Body: %s" % (resp.status_code, resp.text))

        handle_error(resp)
        
        try:
            json_dict = resp.json()
            return json_dict
        except ValueError as e:
            LOG.exception("API returned corrupted message")
            raise exception.S2aApiException("API returned corrupted message: " + str(e))
        
