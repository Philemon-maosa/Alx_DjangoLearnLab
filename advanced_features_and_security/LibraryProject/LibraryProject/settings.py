import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "insecure-secret-key")

# Toggle debug with environment variable (default True for dev)
DEBUG = os.getenv("DJANGO_DEBUG", "True") == "True"

# Allowed hosts
if DEBUG:
    ALLOWED_HOSTS = ["*"]  # Easier for local development
else:
    ALLOWED_HOSTS = ["yourdomain.com", "www.yourdomain.com", "127.0.0.1", "localhost"]

# ---------------------------
# 🔒 Security Settings
# ---------------------------
SECURE_BROWSER_XSS_FILTER = not DEBUG       # Helps mitigate XSS
SECURE_CONTENT_TYPE_NOSNIFF = not DEBUG     # Prevents MIME-type sniffing
X_FRAME_OPTIONS = "DENY"                    # Prevents clickjacking

CSRF_COOKIE_SECURE = not DEBUG              # Only send CSRF cookie over HTTPS in production
SESSION_COOKIE_SECURE = not DEBUG           # Only send session cookie over HTTPS in production
CSRF_COOKIE_HTTPONLY = not DEBUG            # Block JS access to CSRF cookie
SESSION_COOKIE_HTTPONLY = not DEBUG         # Block JS access to session cookie

SECURE_SSL_REDIRECT = not DEBUG             # Redirect HTTP → HTTPS in production

# HSTS (Strict Transport Security) - Production only
SECURE_HSTS_SECONDS = 31536000 if not DEBUG else 0
SECURE_HSTS_INCLUDE_SUBDOMAINS = not DEBUG
SECURE_HSTS_PRELOAD = not DEBUG
