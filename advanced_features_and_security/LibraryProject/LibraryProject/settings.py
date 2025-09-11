# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False   # ✅ Always False in production

# ✅ Change to your actual domain(s) or server IP in production
ALLOWED_HOSTS = ["yourdomain.com", "www.yourdomain.com", "127.0.0.1", "localhost"]

# Security middleware is already included, now configure protections:
SECURE_BROWSER_XSS_FILTER = True   # Helps mitigate XSS attacks
SECURE_CONTENT_TYPE_NOSNIFF = True # Prevents MIME-type sniffing
X_FRAME_OPTIONS = "DENY"           # Prevents clickjacking

# Cookies security
CSRF_COOKIE_SECURE = True          # Ensures CSRF cookie is only sent via HTTPS
SESSION_COOKIE_SECURE = True       # Ensures session cookie is only sent via HTTPS
CSRF_COOKIE_HTTPONLY = True        # Blocks JS access to CSRF cookie
SESSION_COOKIE_HTTPONLY = True     # Blocks JS access to session cookie

# Force HTTPS
SECURE_SSL_REDIRECT = True         # Redirect all HTTP requests to HTTPS

# HSTS (strict transport security)
SECURE_HSTS_SECONDS = 31536000     # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
