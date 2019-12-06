from .common import*

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['106.53.20.146', "127.0.0.1"]
QRURL_ENDPOINT = 'http://106.53.20.146'