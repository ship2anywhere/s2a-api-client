import logging
import argparse
import json

from s2a_api import logutil
from s2a_api import order
from s2a_api.exception import S2aApiException

LOG = logging.getLogger(__name__)

DEFAULT_LOG_LEVEL = "info"

def parse_args():
    """ Parse command line arguments """
    parser = argparse.ArgumentParser(description="Call Ship2Anywhere cancel order service")
    parser.add_argument('--api_url', help='Api url', required=True)
    parser.add_argument('--token', help='Access Token', required=True)
    parser.add_argument('--order_id', help='ID', required=True)
    parser.add_argument('--log', help='Log level, default: %s' % DEFAULT_LOG_LEVEL,
        default=DEFAULT_LOG_LEVEL)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    log_level = logutil.LOG_LEVELS.get(args.log.lower(), logging.INFO)
    logutil.setup_logger(log_level)
    document_service = doc.DocumentService(args.api_url)
        
    try:
        r = document_service.download_documents(args.order_id, args.token)
        print json.dumps(r, indent=4)
    except S2aApiException as e:
        LOG.error(str(e.code) + ": " + str(e))
        exit(1)
    except Exception as e:
        LOG.error(e)
        exit(1)

    exit(0)
