import os
from .settings import *

DEBUG = False

ALLOWED_HOSTS = ['backend']

EXTRA_ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS')
if EXTRA_ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(EXTRA_ALLOWED_HOSTS)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"

        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
    },
}
