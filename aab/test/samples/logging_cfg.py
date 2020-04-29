LOGGING = {
    'version': 1,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(message)s',
        },
        'verbose': {
            'format': '%(asctime)s %(levelname)s %(hostname)s %(process)d %(message)s',
        },
        
        # this is the same as the default, so you can skip configuring it
        'partition_key': {
            'format': '%(asctime)s',
            'datefmt': '%Y%m%d%H%M',
        },
        # this is the same as the default, so you can skip configuring it
        'row_key': {
            'format': '%(asctime)s%(msecs)03d-%(hostname)s-%(process)d-%(rowno)02d',
            'datefmt': '%Y%m%d%H%M%S',
        },
    },
    'filters': {
        'special': {
            '()': 'project.logging.SpecialFilter',
            'foo': 'bar',
        }
    },
    'handlers': {
        'file': {
            'account_name': 'mystorageaccountname',
            'account_key': 'mystorageaccountkey',
            'protocol': 'https',
            'level': 'DEBUG',
            'class': 'azure_storage_logging.handlers.BlobStorageTimedRotatingFileHandler',
            'formatter': 'verbose',
            'filename': 'example.log',
            'when': 'D',
            'interval': 1,
            'container': 'logs-%(hostname)s',
            'zip_compression': False,
        },
        'queue': {
            'account_name': 'mystorageaccountname',
            'account_key': 'mystorageaccountkey',
            'protocol': 'https',
            'queue': 'logs',
            'level': 'CRITICAL',
            'class': 'azure_storage_logging.handlers.QueueStorageHandler',
            'formatter': 'verbose',
        },
        'table': {
            'account_name': 'mystorageaccountname',
            'account_key': 'mystorageaccountkey',
            'protocol': 'https',
            'table': 'logs',
            'level': 'INFO',
            'class': 'azure_storage_logging.handlers.TableStorageHandler',
            'formatter': 'simple',
            'batch_size': 20,
            'extra_properties': ['%(hostname)s', '%(levelname)s'],
            'partition_key_formatter': 'cfg://formatters.partition_key',
            'row_key_formatter': 'cfg://formatters.row_key',
        },
    },
    'loggers': {
        'example': {
            'handlers': ['file', 'queue', 'table'],
            'level': 'DEBUG',
        },
    }
}