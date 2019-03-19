DEFAULT_LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'file': {
            'format': '%(asctime)s %(levelname)s %(filename)s[line:%(lineno)d] %(message)s'
        },
    },
    'handlers': {
        'default': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
        'file_handler': {
            'level': 'INFO',
            'formatter': 'file',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'log.txt',
            'encoding': 'utf8',
            'maxBytes': 1048576,
            'backupCount': 10,
        },
    },
    'loggers': {
        '': {  # root logger
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'app': {
            'handlers': ['file_handler'],
            'level': 'INFO',
            'propagate': False
        },
    }
}