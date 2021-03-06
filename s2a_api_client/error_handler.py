import requests
import exception
import logging

LOG = logging.getLogger(__name__)

def  handle_error(resp, success_codes=(200,)):
    if resp.status_code in success_codes:
        return
        
    elif resp.status_code == requests.codes['BAD_REQUEST']:
        msg = __json_check('BAD_REQUEST', resp)
        LOG.error(msg)
        raise exception.RequestException(msg, 400)
        
    elif resp.status_code == requests.codes['FORBIDDEN'] :
        msg = __json_check('FORBIDDEN', resp)
        LOG.error(msg)
        raise exception.AccessException(msg)
        
    elif resp.status_code == requests.codes['NOT_FOUND'] :
        msg = __json_check('BAD_REQUEST', resp)
        LOG.error(msg)
        raise exception.NotFoundException(msg)

    elif resp.status_code == requests.codes['METHOD_NOT_ALLOWED'] :
        msg = __json_check('METHOD_NOT_ALLOWED', resp)
        LOG.error(msg)
        raise exception.RequestException(msg, 405)
        
    elif resp.status_code == requests.codes['PRECONDITION_FAILED'] :
        msg = __json_check('PRECONDITION_FAILED', resp)
        LOG.error(msg)
        raise exception.ServiceLogicException(msg)
        
    elif resp.status_code == requests.codes['SERVER_ERROR'] :
        msg = __json_check('SERVER_ERROR', resp)
        LOG.error(msg)
        raise exception.ServerException(msg)
        
    else:
        LOG.warning("Unexpected return code: %s" % resp.status_code)
        # msg = __json_check('Unexpected Status Code', resp)
        # raise exception.S2aApiHttpException(msg, resp.status_code)

def __json_check(error_type, resp):
    msg = error_type
    try:
        json_dict = resp.json()
        #if json_dict.has_key('error'):
        #    msg += ": " + json_dict.get('error')
        if json_dict.has_key('message'):
            msg += ": " + json_dict.get('message')
    except ValueError:
        #LOG.exception("API returned corrupted message")
        pass
    return msg
