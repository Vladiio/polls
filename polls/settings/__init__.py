from .base import *

from .production import *

try:
    from .localsettings import *
except ImportError:
    pass
