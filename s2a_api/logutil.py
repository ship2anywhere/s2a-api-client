import logging

LOG_LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,}

def setup_logger(level=logging.INFO):
    # undo the effect of a call to logging.disable(lvl)
    logging.disable(logging.NOTSET)
    # create formatter
    formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(name)s - %(message)s')
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    # add ch to logger
    root_logger = logging.getLogger()
    root_logger.addHandler(ch)
    root_logger.setLevel(level)
