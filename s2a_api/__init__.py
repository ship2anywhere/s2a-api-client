from quote import QuoteService
from order import OrderService
from doc import DocumentService
from track import TrackService
from util import append_slash

class S2aApi(object):
    """ This class allows to create all API service objects in single place.
        Simplifies instantiation and access to API services.
    """
    
    def __init__(self, api_url, verify_cert = False):
        self.api_url = append_slash(api_url)
        self.verify_cert= verify_cert
        self.quote_service = QuoteService(api_url, verify_cert)
        self.order_servive = OrderService(api_url, verify_cert)
        self.doc_servive = DocumentService(api_url, verify_cert)
        self.track_servive = TrackService(api_url, verify_cert)
