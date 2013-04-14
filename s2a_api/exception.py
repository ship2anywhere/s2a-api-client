class S2aApiException(Exception):
    def __init__(self, msg):
        Exception.__init__(self, msg)
        
class S2aApiHttpException(S2aApiException):
    def __init__(self, msg, code):
        self.code = code
        S2aApiException.__init__(self, msg)
    def __str__(self):
        return "%s: %s" % (self.code, self.message)

class ServerException(S2aApiHttpException):
    """500"""
    def __init__(self, msg):
        S2aApiHttpException.__init__(self, msg, 500)

class RequestException(S2aApiHttpException):
    """400; 405"""
    def __init__(self, msg, code):
        S2aApiHttpException.__init__(self, msg, code)

class AccessException(S2aApiHttpException):
    """403"""
    def __init__(self, msg):
        S2aApiHttpException.__init__(self, msg, 403)

class NotFoundException(S2aApiHttpException):
    """404"""
    def __init__(self, msg):
        S2aApiHttpException.__init__(self, msg, 404)

class ServiceLogicException(S2aApiHttpException):
    """412"""
    def __init__(self, msg):
        S2aApiHttpException.__init__(self, msg, 412)
