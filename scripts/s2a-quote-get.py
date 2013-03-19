import logging
import argparse

from s2a_api import logutil
from s2a_api import quote

LOG = logging.getLogger(__name__)

DEFAULT_LOG_LEVEL = "info"

def parse_args():
    """ Parse command line arguments """
    parser = argparse.ArgumentParser(description="Call Ship2Anywhere quote service")
    parser.add_argument('--api_url', help='Api url', required=True)
    parser.add_argument('--json_file', help='Json data', required=True)
    parser.add_argument('--log', help='Log level, default: %s' % DEFAULT_LOG_LEVEL,
        default=DEFAULT_LOG_LEVEL)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    log_level = logutil.LOG_LEVELS.get(args.log.lower(), logging.INFO)
    logutil.setup_logger(log_level)
    quote_service = quote.QuoteService(args.api_url)

    #TODO - add arg control
    sample_file_name = args.json_file
    try:
        json_data = eval(open(sample_file_name).read())
        #logutil.info('File ' + sample_file_name + 'opened')
    except IOError:
        print 'cannot open', sample_file_name
        exit()
    except SyntaxError:
        print 'file is not in json format'
        exit()
        
    r = quote_service.get_quote(json_data)
    print r
    

    # TODO
