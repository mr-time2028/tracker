from .base import *

try:
    from app.config.settings.local import *
except Exception:
    pass


# Django debug toolbar settings
INSTALLED_APPS += ["debug_toolbar",]
INTERNAL_IPS = ["127.0.0.1",]
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware",]
