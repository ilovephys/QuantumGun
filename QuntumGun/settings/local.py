# settings/local.py

from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ilpfk&p8cokt%o%q@r12^46q*jxvjqyi8ixf1u#vlr=!fardi9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

STATIC_ROOT = "/usr/share/nginx/html/static"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LOGGING = {
    "version": 1,
    "disable_existing_loggers":False,

    "loggers":{
        "django":{
            "handlers": ["console"],
            "level": "INFO",
        },
        "QuntumGun":{
            "handlers": ["console"],
            "level": "DEBUG",
        },
    },

    "handlers":{
        "console":{
            "level":"DEBUG",
            "class":"logging.StreamHandler",
            "formatter":"dev"
        },
    },
    "formatters":{
        "dev":{
            "format":"¥t".join([
                "%(asctime)s",
                "[%(levelname)s]",
                "%(pathname)s(Line:%(lineno)d)",
                "%(message)s"
            ])
        },
    }
}