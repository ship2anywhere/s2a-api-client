import logging
import json
import requests

LOG = logging.getLogger(__name__)

class QuoteService(object):
  
    def __init__(self, api_url):
        self.api_url = api_url

    def get_quote(self, request):
        """ Get quote """
        LOG.info("Calling quote service")
        req = {"request": request}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        #print json.dumps(request)
        #resp = requests.post(url=self.api_url, data=json.dumps(request), headers=headers, verify=False)
        resp = requests.post(url=self.api_url, data=json.dumps(req), headers=headers, verify=False)
        if resp.status_code == 200:
            try:
                return resp.json()
            except ValueError:
                print "not a json response"
        else:
            #TODO raise exceptions
            return 2
