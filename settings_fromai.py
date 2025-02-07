INSTALLED_APPS = [
    # ...existing code...
    'oauth2_provider',
    'rest_framework',
    # ...existing code...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

OAUTH2_PROVIDER = {
    'ACCESS_TOKEN_EXPIRE_SECONDS': 36000,
    'AUTHORIZATION_CODE_EXPIRE_SECONDS': 600,
    'REFRESH_TOKEN_EXPIRE_SECONDS': 86400,
}
