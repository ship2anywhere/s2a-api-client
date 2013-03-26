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
            
        elif resp.status_code == requests.codes['BAD_REQUEST']:
            # assert resp.status_code == resp.json().get('code'), "Return Codes do not match."
            msg = self.__json_check('BAD_REQUEST', resp)
            LOG.error(msg)
            raise exception.RequestException(msg, 400)
            
        elif resp.status_code == requests.codes['FORBIDDEN'] :
            msg = self.__json_check('FORBIDDEN')
            LOG.error(msg)
            raise exception.AccessException(msg)
            
        elif resp.status_code == requests.codes['NOT_FOUND'] :
            msg = self.__json_check('BAD_REQUEST')
            LOG.error(msg)
            raise exception.RequestException(msg)

        elif resp.status_code == requests.codes['METHOD_NOT_ALLOWED'] :
            msg = self.__json_check('METHOD_NOT_ALLOWED')
            LOG.error(msg)
            raise exception.RequestException(msg, 405)
            
        elif resp.status_code == requests.codes['PRECONDITION_FAILED'] :
            msg = self.__json_check('PRECONDITION_FAILED')
            LOG.error(msg)
            raise exception.ServiceLogicException(msg)
            
        elif resp.status_code == requests.codes['SERVER_ERROR'] :
            msg = self.__json_check('SERVER_ERROR')
            LOG.error(msg)
            raise exception.ServerException(msg)

    def __json_check(self, error_type, resp):
        msg = error_type
        try:
            print "asdf"
            json_dict = resp.json()
            if json_dict.has_key('message'):
                msg += ": " + json_dict.get('message')
        except ValueError:
            LOG.exception("API returned corrupted message")
        return msg
