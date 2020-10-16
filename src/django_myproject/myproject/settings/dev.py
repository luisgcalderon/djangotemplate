import os
os.environ.setdefault('PROJECT_ENV', 'DEVELOPMENT')

from ._base import *

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"