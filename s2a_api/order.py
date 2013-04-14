import logging
import json
import requests
import exception
from error_handler import handle_error

LOG = logging.getLogger(__name__)

class OrderService(object):
  
    def __init__(self, api_url):
        self.api_url = api_url

    def create_order(self, request, token):
        """ Create order """
        LOG.info("Calling order service")
        req = {"request": request}
        headers = {'Content-Type': 'application/json',
                   'charset': 'UTF-8',
                   "Authorization": "Bearer " + token}

        resp = requests.post(url=self.api_url, data=json.dumps(req), headers=headers, verify=False)

        handle_error(resp)
        
        try:
            json_dict = resp.json()
            LOG.info("Response code = " + str(resp.status_code))
            return json_dict
        except ValueError:
            LOG.exception("API returned corrupted message")
            raise

    def accept_order(self, request, order_id, token):
        # if IDs have to be equal. If so, then does it need to be parsed?
        # Answer: has to be, but it is not required in JSON
        """ Accept order """
        LOG.info("Calling order service")
        req = {"request": request}
        url = self.api_url + order_id + "/accept"
        headers = {'Content-Type': 'application/json',
                   'charset': 'UTF-8',
                   "Authorization": "Bearer " + token}

        resp = requests.post(url=url, data=json.dumps(req), headers=headers, verify=False)

        handle_error(resp)
        
        try:
            json_dict = resp.json()
            LOG.info("Response code = " + str(resp.status_code))
            return json_dict
        except ValueError:
            LOG.exception("API returned corrupted message")
            raise
            
    def cancel_order(self, order_id, token):
        """ Cancel order """
        LOG.info("Calling order service")
        url = self.api_url + order_id
        headers = {"Authorization": "Bearer " + token}

        resp = requests.delete(url=url, headers=headers, verify=False)

        handle_error(resp)
        
        try:
            json_dict = resp.json()
            LOG.info("Response code = " + str(resp.status_code))
            return json_dict
        except ValueError:
            LOG.exception("API returned corrupted message")
            raise            
            
    def fetch_order(self, order_id, token):
        """ Fetch order """
        LOG.info("Calling order service")
        url = self.api_url + order_id
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
