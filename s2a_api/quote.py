import logging
import json

LOG = logging.getLogger(__name__)

class QuoteService(object):
  
    def __init__(self, api_url):
        self.api_url = api_url

    def get_quote(self, request):
        """ Get quote """
        LOG.info("Calling quote service")
        json.dumps({"request": request})
