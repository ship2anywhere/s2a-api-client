# S2A API Client common functions

import requests
import logging
import json
import exception
from error_handler import handle_error

LOG = logging.getLogger(__name__)

def api_call(method, url, data='', headers={}, token=None, 
        verify_cert=False, success_codes=(200,)):
    """ General function which can call any S2A API service """
    
    if token:
        headers["Authorization"] = "Bearer %s" % token
        
    if LOG.isEnabledFor(logging.DEBUG):
        LOG.debug("Request URL: %s ; method: %s ; Request Data: %s ; Request Token: %s" \
            % (url, method, data, token))
            
    resp = requests.request(method, url, data=data, headers=headers, verify=verify_cert)
    
    if LOG.isEnabledFor(logging.DEBUG):
        LOG.debug("Status Code: %s; Response Body: %s" % (resp.status_code, resp.text))
        
    handle_error(resp, success_codes)
    
    try:
        return resp.json()
    except ValueError as e:
        LOG.exception("API returned corrupted message")
        raise S2aApiException("API returned corrupted message: %s" % e)

def append_slash(url):
    """ Function which return URL ended with the slash "/" """
    if url[-1] == "/":
        return url
    return url + "/"
        
