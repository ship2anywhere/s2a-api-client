from quote import QuoteService


class S2aApi(object):
    
    def __init__(self, api_url):
        self.api_url = api_url
        self.quote_service = QuoteService(api_url)
        self.order_servive = OrderService(api_url)
        self.doc_servive = OrderService(api_url)
        self.track_servive = OrderService(api_url)
        # TODO add more
