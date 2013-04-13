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

    def accept_order(self, request, token):
        # TODO: ask if IDs have to be equal. If so, then does it need to be parsed?
        pass
        """ Accept order """
        LOG.info("Calling order service")
        req = {"request": request}
        headers = {'Content-Type': 'application/json',
                   'charset': 'UTF-8',
                   "Authorization": "Bearer " + token}

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
            
    def cancel_order(self, id, token):
        """ Accept order """
        LOG.info("Calling order service")
        url = self.api_url + id
        headers = {"Authorization": "Bearer " + token}

        resp = requests.delete(url=url, headers=headers, verify=False)

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
            
    def fetch_order(self, id, token):
        """ Fetch order """
        LOG.info("Calling order service")
        url = self.api_url + id
        headers = {"Authorization": "Bearer " + token}

        resp = requests.get(url=url, headers=headers, verify=False)

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

    def download_documents(self, id, token):
        """ Download documents """
        LOG.info("Calling order service")
        url = self.api_url + id + "/documents"
        headers = {"Authorization": "Bearer " + token}

        resp = requests.get(url=url, headers=headers, verify=False)

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
