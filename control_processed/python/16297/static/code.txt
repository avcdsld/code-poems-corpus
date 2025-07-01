def init_logger():
    """
    Initialize the logging configuration for the turicreate package.

    This does not affect the root logging config.
    """
    import logging as _logging
    import logging.config

    # Package level logger
    _logging.config.dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'standard': {
                'format': '%(asctime)s [%(levelname)s] %(name)s, %(lineno)s: %(message)s'
            },
            'brief': {
                'format': '[%(levelname)s] %(name)s: %(message)s'
            }
        },
        'handlers': {
            'default': {
                'class': 'logging.StreamHandler',
                'formatter': 'brief'
            },
            'file': {
                'class': 'logging.FileHandler',
                'formatter': 'standard',
                'filename': _client_log_file,
                'encoding': 'UTF-8',
                'delay': 'False',
            }
        },
        'loggers': {
            _root_package_name: {
                'handlers': ['default', 'file'],
                'propagate': 'True'
            }
        }
    })

    # Set module specific log levels
    _logging.getLogger('requests').setLevel(_logging.CRITICAL)
    if _i_am_a_lambda_worker():
        _logging.getLogger(_root_package_name).setLevel(_logging.WARNING)
    else:
        _logging.getLogger(_root_package_name).setLevel(_logging.INFO)