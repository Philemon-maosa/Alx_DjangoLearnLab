from .base import *

DEBUG = True

ALLOWED_HOSTS = ['*']

# Static and media files
STATICFILES_DIRS = [BASE_DIR / "static"]
MEDIA_ROOT = BASE_DIR / "media"

# Database: uses SQLite by default (from base)
