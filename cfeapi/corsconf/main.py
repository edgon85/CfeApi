CORS_URLS_REGEX = r'^/api/.*$'
CORS_ORIGIN_WHITELIST = (
    'localhost:4200',
    '127.0.0.1'
)

from corsheaders.defaults import default_methods

CORS_ALLOW_METHODS = default_methods + (
    'X-CSRFToken',
)