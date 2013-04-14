import logging
import json
import requests
import exception
from error_handler import handle_error
from slash_appender import append_slash

LOG = logging.getLogger(__name__)

class TrackService(object):
  
    def __init__(self, api_url):
        self.api_url = append_slash(api_url)

    def track(self, tracking_number):
        """ Track """
        LOG.info("Calling track service")
        url = self.api_url + tracking_number + "/"
        resp = requests.get(url=url, verify=False)

        handle_error(resp)
        
        try:
            json_dict = resp.json()
            LOG.info("Response code = " + str(resp.status_code))
            return json_dict
        except ValueError as e:
            LOG.exception("API returned corrupted message")
            raise exception.S2aApiException("API returned corrupted message: " + str(e))
        
