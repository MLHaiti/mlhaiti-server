# In order to disallow django environ 
# to read .env file in base settings
# when travis are running
CI = True 

import os

from .base import * 

import dj_database_url

SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

DATABASES = {'default': dj_database_url.config()}