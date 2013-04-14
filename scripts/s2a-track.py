import logging
import argparse
import json

from s2a_api import logutil
from s2a_api import track
from s2a_api.exception import S2aApiException

LOG = logging.getLogger(__name__)

DEFAULT_LOG_LEVEL = "info"

def parse_args():
    """ Parse command line arguments """
    parser = argparse.ArgumentParser(description="Call Ship2Anywhere fetch order service")
    parser.add_argument('--api_url', help='Api url', required=True)
    parser.add_argument('--tracking_number', help='Tracking Number', required=True)
    parser.add_argument('--log', help='Log level, default: %s' % DEFAULT_LOG_LEVEL,
        default=DEFAULT_LOG_LEVEL)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    log_level = logutil.LOG_LEVELS.get(args.log.lower(), logging.INFO)
    logutil.setup_logger(log_level)
    track_service = track.TrackService(args.api_url)
        
    try:
        r = track_service.track(args.tracking_number)
        print json.dumps(r, indent=4)
    except Exception as e:
        LOG.error(e)
        exit(1)

    exit(0)
