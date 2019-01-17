from .is_development import is_development
from .installed_apps import *

if is_development:
    from .development import *
    print('Development Mode')
else:
    from .production import *
    print('Production Mode')