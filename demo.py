from logger import builder

builder = builder.Builder()
logger = builder.get_logger('app')

logger.debug('debug message')
logger.info('info message')
logger.warn('warn message')
logger.error('error message')
logger.critical('critical message')