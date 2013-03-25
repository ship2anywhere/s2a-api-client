class S2aApiException(Exception):
    def __init__(self, msg, code):
        self.code = code
        Exception.__init__(self, msg)

class ServerException(S2aApiException):
    """500"""
    def __init__(self, msg):
        S2aApiException.__init__(self, msg, 500)

class RequestException(S2aApiException):
    """400; 405"""
    def __init__(self, msg, code):
        S2aApiException.__init__(self, msg, code)

class AccessException(S2aApiException):
    """403"""
    def __init__(self, msg):
        S2aApiException.__init__(self, msg, 403)

class NotFoundException(S2aApiException):
    """404"""
    def __init__(self, msg):
        S2aApiException.__init__(self, msg, 404)

class ServiceLogicException(S2aApiException):
    """412"""
    def __init__(self, msg):
        S2aApiException.__init__(self, msg, 412)
