import logging
import json
import requests
import exception
from error_handler import handle_error
from slash_appender import append_slash

LOG = logging.getLogger(__name__)

class QuoteService(object):
  
    def __init__(self, api_url):
        self.api_url = append_slash(api_url)

    def get_quote(self, request):
        """ Get quote """
        LOG.info("Calling quote service")
        req = {"request": request}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        resp = requests.post(url=self.api_url, data=json.dumps(req), headers=headers, verify=False)

        handle_error(resp)

        try:
            json_dict = resp.json()
            LOG.info("Response code = " + str(resp.status_code))
            return json_dict
        except ValueError:
            LOG.exception("API returned corrupted message")
            raise S2aApiException("API returned corrupted message: " + str(e))

