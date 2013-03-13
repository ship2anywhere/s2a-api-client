import logging
import argparse

from s2a_api import logutil
from s2a_api import quote

LOG = logging.getLogger(__name__)

DEFAULT_LOG_LEVEL = "info"

def parse_args():
    """ Parse command line arguments """
    parser = argparse.ArgumentParser(description="Call Ship2Anywhere quote service")
    parser.add_argument('--api_url', help='Tornado server bind port', required=True)
    parser.add_argument('--log', help='Log level, default: %s' % DEFAULT_LOG_LEVEL,
        default=DEFAULT_LOG_LEVEL)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    log_level = logutil.LOG_LEVELS.get(args.log.lower(), logging.INFO)
    logutil.setup_logger(log_level)
    quote_service = quote.QuoteService(args.api_url)
    # TODO
