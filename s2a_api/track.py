import logging
from util import append_slash
from util import api_call

LOG = logging.getLogger(__name__)

class TrackService(object):
  
    def __init__(self, api_url, verify_cert = False):
        self.api_url = append_slash(api_url)
        self.verify_cert = verify_cert

    def track(self, tracking_number):
        """ Track """
        url = self.api_url + "track/" + tracking_number + "/"
        
        return api_call("get", url)
