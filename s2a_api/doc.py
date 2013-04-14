import logging
import json
import requests
import exception
from error_handler import handle_error

LOG = logging.getLogger(__name__)

class DocumentService(object):
  
    def __init__(self, api_url):
        self.api_url = api_url

    def download_documents(self, order_id, token):
        """ Download documents """
        LOG.info("Calling order service")
        url = self.api_url + order_id + "/documents"
        headers = {"Authorization": "Bearer " + token}

        resp = requests.get(url=url, headers=headers, verify=False)

        handle_error(resp)
        
        try:
            json_dict = resp.json()
            LOG.info("Response code = " + str(resp.status_code))
            return json_dict
        except ValueError:
            LOG.exception("API returned corrupted message")
            raise
