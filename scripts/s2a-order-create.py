import logging
import argparse
import json

from s2a_api_client import logutil
from s2a_api_client import order
from s2a_api_client.exception import S2aApiException

LOG = logging.getLogger(__name__)

DEFAULT_LOG_LEVEL = "info"

def parse_args():
    """ Parse command line arguments """
    parser = argparse.ArgumentParser(description="Call Ship2Anywhere make order service")
    parser.add_argument('--api_url', help='Api url', required=True)
    parser.add_argument('--token', help='Access Token', required=True)
    parser.add_argument('--json_file', help='Json data', required=True)
    parser.add_argument('--log', help='Log level, default: %s' % DEFAULT_LOG_LEVEL,
        default=DEFAULT_LOG_LEVEL)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    log_level = logutil.LOG_LEVELS.get(args.log.lower(), logging.INFO)
    logutil.setup_logger(log_level)
    order_service = order.OrderService(args.api_url)

    try:
        with open(args.json_file): pass
    except IOError:
        LOG.error("File " + args.json_file +" does not exist")
        exit(1)
        
    sample_file_name = args.json_file
    try:
        json_data = json.load(open(sample_file_name))
        LOG.info('File ' + sample_file_name + ' opened')
    except IOError:
        LOG.error('cannot open ', sample_file_name)
        exit(1)
    except ValueError:
        LOG.error('File is not in JSON format')
        exit(1)
        
    try:
        r = order_service.create_order(json_data, args.token)
        print json.dumps(r, indent=4)
    except Exception as e:
        LOG.error(e)
        exit(1)

    exit(0)
