#!/usr/bin/env python

import logging
import argparse
import json

from s2a_api_client import logutil
from s2a_api_client import auth
from s2a_api_client.exception import S2aApiException

LOG = logging.getLogger(__name__)

DEFAULT_LOG_LEVEL = "info"

def parse_args():
    """ Parse command line arguments """
    parser = argparse.ArgumentParser(description="Call Ship2Anywhere auth service")
    parser.add_argument('--api_url', help='Api url', required=True)
    parser.add_argument('--client_id', help='Client ID', required=True)
    parser.add_argument('--client_secret', help='Client Secret', required=True)
    parser.add_argument('--code', help='OAuth2.0 CODE', required=True)
    parser.add_argument('--log', help='Log level, default: %s' % DEFAULT_LOG_LEVEL,
        default=DEFAULT_LOG_LEVEL)
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    log_level = logutil.LOG_LEVELS.get(args.log.lower(), logging.INFO)
    logutil.setup_logger(log_level)
    auth_service = auth.AuthService(args.api_url, args.client_id, args.client_secret)
        
    try:
        r = auth_service.get_token(args.code)
        
        print json.dumps(r, indent=4)
    except Exception as e:
        LOG.error(e)
        exit(1)

    exit(0)
