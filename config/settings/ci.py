import os

from .base import * 

import dj_database_url

SECRET_KEY = os.environ["SECRET_KEY"]

DATABASES = {'default': dj_database_url.config()}