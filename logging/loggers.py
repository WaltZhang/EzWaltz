import logging
from logging.handlers import RotatingFileHandler, SMTPHandler

file_handler = RotatingFileHandler('logs/log.txt', maxBytes=1*1024*1024, backupCount=100)

# configly format to the log messages
formatter = logging.Formatter("[%(asctime)s]  %(levelname)s {%(pathname)s:%(lineno)d}: %(message)s")
file_handler.setFormatter(formatter)
