from .base import *
import dj_database_url
import os

DEBUG = False

# Heroku dynamically assigns the domain, so use environment variable
ALLOWED_HOSTS = ["*"]

# --------------------------------------
# Database Configuration (Heroku)
# --------------------------------------
# Heroku provides DATABASE_URL — we'll use it for PostgreSQL
DATABASES = {
    "default": dj_database_url.config(default=os.environ.get("DATABASE_URL"))
}

# --------------------------------------
# Security Settings
# --------------------------------------
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = "DENY"
SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# --------------------------------------
# Static Files with WhiteNoise
# --------------------------------------
STATIC_ROOT = BASE_DIR / "staticfiles"
STATIC_URL = "/static/"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# --------------------------------------
# Logging (optional but useful for Heroku)
# --------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}
