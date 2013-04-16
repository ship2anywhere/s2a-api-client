import logging
from util import append_slash
from util import api_call

LOG = logging.getLogger(__name__)

class DocumentService(object):
  
    def __init__(self, api_url, verify_cert = False):
        self.api_url = append_slash(api_url)
        self.verify_cert = verify_cert

    def download_documents(self, order_id, token):
        """ Download documents """
        url = self.api_url + order_id + "/documents/"
        
        return api_call("get", url, token=token)
