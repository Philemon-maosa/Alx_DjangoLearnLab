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

# ✅ Detect HTTPS correctly when behind a proxy/load balancer
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
