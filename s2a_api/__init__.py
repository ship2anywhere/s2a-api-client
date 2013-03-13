from quote import QuoteService


class S2aApi(object):
    
    def __init__(self, api_url):
        self.quote = QuoteService(api_url)
        # TODO add more
