import logging
import json
import requests
import exception

LOG = logging.getLogger(__name__)

class AuthService(object):
    
    def __init__(self, api_url, client_id, client_secret):
        self.api_url = api_url
        self.client_id = client_id
        self.client_secret = client_secret
    
    def get_token(self, code):
        """ Get token """
        LOG.info("Calling authentication service")
        
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        
        data = {
            'grant_type': 'authorization_code',
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'code': code
            }
            
        resp = requests.post(url=self.api_url, data=data, headers=headers, verify=False)
        
        if resp.status_code == 200:
            try:
                json_dict = resp.json()
                LOG.info("Response code = " + str(resp.status_code))
                if json_dict.has_key('access_token'):
                    return str(json_dict.get('access_token'))
                else:
                    raise Exception
            except ValueError, Exception:
                LOG.exception("API returned corrupted message")
                raise
                
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
            raise exception.NotFoundException(msg)

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
            json_dict = resp.json()
            if json_dict.has_key('error'):
                msg += ": " + json_dict.get('error')
            elif json_dict.has_key('message'):
                msg += ": " + json_dict.get('message')
        except ValueError:
            LOG.exception("API returned corrupted message")
        return msg
        
