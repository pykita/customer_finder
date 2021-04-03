import logging

log_format = '%(asctime).19s | %(levelname)s | %(filename)s#%(funcName)s -- %(message)s'
logging.basicConfig(level=logging.INFO, format=log_format)

log = logging.getLogger()