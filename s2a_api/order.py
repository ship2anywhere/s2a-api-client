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
        url = self.api_url + "orders/"
        req = {"request": request}
        headers = {'Content-Type': 'application/json',
                   'charset': 'UTF-8'}

        return api_call("post", url, data=json.dumps(req), headers=headers, token=token, verify_cert=self.verify_cert)
        
    def accept_order(self, request, order_id, token):
        """ Accept order """
        url = self.api_url + "orders/" + order_id + "/accept/"
        req = {"request": request}
        headers = {'Content-Type': 'application/json',
                   'charset': 'UTF-8'}

        return api_call("put", url, data=json.dumps(req), headers=headers, token=token, verify_cert=self.verify_cert, success_codes=(200, 201))
            
    def cancel_order(self, order_id, token):
        """ Cancel order """
        url = self.api_url + "orders/" + order_id + "/"
        
        return api_call("delete", url, token=token, verify_cert=self.verify_cert)
            
    def fetch_order(self, order_id, token):
        """ Fetch order """
        url = self.api_url + "orders/" + order_id + "/"
        
        return api_call("get", url, token=token, verify_cert=self.verify_cert)
