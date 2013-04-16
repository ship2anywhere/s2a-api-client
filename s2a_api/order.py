import logging
import json
import requests
import exception
from error_handler import handle_error
from util import append_slash

LOG = logging.getLogger(__name__)

class OrderService(object):
  
    def __init__(self, api_url, verify_cert = False):
        self.api_url = append_slash(api_url)
        self.verify_cert = verify_cert

    def create_order(self, request, token):
        """ Create order """
        req = {"request": request}
        headers = {'Content-Type': 'application/json',
                   'charset': 'UTF-8',
                   "Authorization": "Bearer " + token}

        if LOG.isEnabledFor(logging.DEBUG):
            LOG.debug("Request URL: %s ; Request Data: %s ; Request Token: %s" % (self.api_url, req, token))
        
        resp = requests.post(url=self.api_url, data=json.dumps(req), headers=headers, verify = verify_cert)
        
        if LOG.isEnabledFor(logging.DEBUG):
            LOG.debug("Status Code: %s; Response Body: %s" % (resp.status_code, resp.text))
        
        handle_error(resp)
        
        try:
            json_dict = resp.json()
            return json_dict
        except ValueError as e:
            LOG.exception("API returned corrupted message")
            raise S2aApiException("API returned corrupted message: " + str(e))

    def accept_order(self, request, order_id, token):
        """ Accept order """
        req = {"request": request}
        url = self.api_url + order_id + "/accept/"
        headers = {'Content-Type': 'application/json',
                   'charset': 'UTF-8',
                   "Authorization": "Bearer " + token}

        if LOG.isEnabledFor(logging.DEBUG):
            LOG.debug("Request URL: %s ; Request Data: %s ; Request Token: %s" % (url, req, token))
        
        resp = requests.put(url=url, data=json.dumps(req), headers=headers, verify = verify_cert)
        
        if LOG.isEnabledFor(logging.DEBUG):
            LOG.debug("Status Code: %s; Response Body: %s" % (resp.status_code, resp.text))

        handle_error(resp, (201,200))
        
        try:
            json_dict = resp.json()
            return json_dict
        except ValueError as e:
            LOG.exception("API returned corrupted message")
            raise S2aApiException("API returned corrupted message: " + str(e))
            
    def cancel_order(self, order_id, token):
        """ Cancel order """
        url = self.api_url + order_id + "/"
        headers = {"Authorization": "Bearer " + token}

        if LOG.isEnabledFor(logging.DEBUG):
            LOG.debug("Request URL: %s ; Request Token: %s" % (url, token))
        
        resp = requests.delete(url=url, headers=headers, verify = verify_cert)
        
        if LOG.isEnabledFor(logging.DEBUG):
            LOG.debug("Status Code: %s; Response Body: %s" % (resp.status_code, resp.text))

        handle_error(resp)
        
        try:
            json_dict = resp.json()
            return json_dict
        except ValueError as e:
            LOG.exception("API returned corrupted message")
            raise S2aApiException("API returned corrupted message: " + str(e))        
            
    def fetch_order(self, order_id, token):
        """ Fetch order """
        url = self.api_url + order_id + "/"
        headers = {"Authorization": "Bearer " + token}

        if LOG.isEnabledFor(logging.DEBUG):
            LOG.debug("Request URL: %s ; Request Token: %s" % (url, token))
            
        resp = requests.get(url=url, headers=headers, verify = verify_cert)
        
        if LOG.isEnabledFor(logging.DEBUG):
            LOG.debug("Status Code: %s; Response Body: %s" % (resp.status_code, resp.text))

        handle_error(resp)

        try:
            json_dict = resp.json()
            return json_dict
        except ValueError as e:
            LOG.exception("API returned corrupted message")
            raise S2aApiException("API returned corrupted message: " + str(e))
