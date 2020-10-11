from .base import * 

import dj_database_url

SECRET_KEY="#&3q+m3rfc7isd#7v+4yqm%obb*s10z)+rxs0^*tr-yx^6(l7m"

DATABASES = {'default': dj_database_url.config()}