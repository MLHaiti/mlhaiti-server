from .base import * 

#setup env 
import environ

env = environ.Env()

try:
    PRODUCTION = env("PRODUCTION")
except:
    PRODUCTION = None

if not PRODUCTION:
    # reading .env file
    environ.Env.read_env(os.path.join(BASE_DIR,'.env'))

SECRET_KEY=env("DJANGO_SECRET_KEY")

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': env("DB_NAME"),
            'USER': env("DB_USER"),
            'PASSWORD': env("DB_PASSWORD"),
            'HOST': env("DB_HOST"),
            'PORT': env("DB_PORT"),
        }
    }