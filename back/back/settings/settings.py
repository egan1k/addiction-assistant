
from back.settings.base_settings import *  # noqa
from back.settings.rest_framework_settings import *  # noqa

try:
    from back.settings.local_settings import *  # noqa
except ImportError:
    pass
