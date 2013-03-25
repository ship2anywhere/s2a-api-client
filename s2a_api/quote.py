import logging
import json
import requests
import exception

LOG = logging.getLogger(__name__)

class QuoteService(object):
  
    def __init__(self, api_url):
        self.api_url = api_url

    def get_quote(self, request):
        """ Get quote """
        LOG.info("Calling quote service")
        req = {"request": request}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        resp = requests.post(url=self.api_url, data=json.dumps(req), headers=headers, verify=False)

        try:
            if resp.status_code == requests.codes['OK']:
                assert resp.status_code == resp.json().get('code'), "Return Codes do not match."
                LOG.info("Response code = " + str(resp.status_code))
                return resp.json()
                
            elif resp.status_code == requests.codes['BAD_REQUEST']:
                assert resp.status_code == resp.json().get('code'), "Return Codes do not match."
                if resp.json().has_key('message'):
                    msg = 'BAD_REQUEST: ' + resp.json().get('message')
                    LOG.error(msg)
                    raise exception.RequestException(msg, 400)
                
            elif resp.status_code == requests.codes['FORBIDDEN'] :
                LOG.error("Response code = " + str(resp.status_code))
                raise exception.AccessException('FORBIDDEN')
                
            elif resp.status_code == requests.codes['NOT_FOUND'] :
                LOG.error("Response code = " + str(resp.status_code))
                raise exception.RequestException('NOT_FOUND', 404)

            elif resp.status_code == requests.codes['METHOD_NOT_ALLOWED'] :
                LOG.error("Response code = " + str(resp.status_code))
                raise exception.RequestException('METHOD_NOT_ALLOWED', 405)
                
            elif resp.status_code == requests.codes['PRECONDITION_FAILED'] :
                LOG.error("Response code = " + str(resp.status_code))
                raise exception.ServiceLogicException('PRECONDITION_FAILED')
                
            elif resp.status_code == requests.codes['SERVER_ERROR'] :
                LOG.error("Response code = " + str(resp.status_code))
                raise exception.ServerException('SERVER_ERROR', 500)

        except ValueError:
            LOG.error("Not a JSON response")
            return 1
