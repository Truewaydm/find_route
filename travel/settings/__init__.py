from .production import *

try:
    from .local_settings import *
except ImportError:
    print('Unable to load local_settings.py:')
