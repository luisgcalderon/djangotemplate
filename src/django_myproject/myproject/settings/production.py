import os
os.environ.setdefault('PROJECT_ENV', 'PRODUCTION')

from ._base import *

WEBSITE_URL = "http://myproject.com" # without trailing slash