import logging
import json
from util import append_slash
from util import api_call

LOG = logging.getLogger(__name__)

class OrderService(object):
  
    def __init__(self, api_url, verify_cert = False):
        self.api_url = append_slash(api_url)
        self.verify_cert = verify_cert

    def create_order(self, request, token):
        """ Create order """
        req = {"request": request}
        headers = {'Content-Type': 'application/json',
                   'charset': 'UTF-8'}

        return api_call("post", self.api_url, data=json.dumps(req), headers=headers, token=token)
        
    def accept_order(self, request, order_id, token):
        """ Accept order """
        req = {"request": request}
        url = self.api_url + order_id + "/accept/"
        headers = {'Content-Type': 'application/json',
                   'charset': 'UTF-8'}

        return api_call("put", url, data=json.dumps(req), headers=headers, token=token, success_codes=(200, 201))
            
    def cancel_order(self, order_id, token):
        """ Cancel order """
        url = self.api_url + order_id + "/"
        
        return api_call("delete", url, token=token)
            
    def fetch_order(self, order_id, token):
        """ Fetch order """
        url = self.api_url + order_id + "/"
        
        return api_call("get", url, token=token)
