from .base import *
import dj_database_url

# Turn off debug in production
DEBUG = False

# Set allowed hosts for production domain
ALLOWED_HOSTS = ["yourdomain.com", "www.yourdomain.com"]

# Security settings
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Static files via WhiteNoise
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Database configuration using DATABASE_URL (Heroku)
DATABASES['default'] = dj_database_url.config(default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}") }
