import logging.config
from logger.config import DEFAULT_LOGGING


class Builder:
    def __init__(self, conf_file=None):
        if conf_file is not None:
            logging.config.fileConfig(conf_file)
        else:
            logging.config.dictConfig(DEFAULT_LOGGING)

    def get_logger(self, logger_name=None):
        if logger_name is not None or logger_name != '':
            return logging.getLogger(logger_name)
        return logging.getLogger('')
