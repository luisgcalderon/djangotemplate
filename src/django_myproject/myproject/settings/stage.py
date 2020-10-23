import os
os.environ.setdefault('PROJECT_ENV', 'STAGE')

from ._base import *

WEBSITE_URL = "http://test.myproject.com" # without trailing slash