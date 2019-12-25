import os
import json
import sys

from .base import BASE_DIR, CLEF_NAME


def dev_settings():
    return 'runserver' in sys.argv


if dev_settings():
    CLEF_PATH = os.path.join(BASE_DIR, f'djiometsa/data/{CLEF_NAME}')
else:
    CLEF_PATH = f'/home/clovis/data/{CLEF_NAME}'


clef = {}
with open(CLEF_PATH, mode='r') as j_clef:
    clef.update(json.load(j_clef))

# Django key
SECRET_KEY = clef['django_key']

# Recaptcha Key
GOOGLE_RECAPTCHA_KEY = clef['recaptcha']
GOOGLE_RECAPTCHA_HTML = clef['recaptchaHtml']

# Email settings
EMAIL_BACKEND = clef['email_backend']
EMAIL_HOST = clef['email_host']
EMAIL_PORT = 465
EMAIL_HOST_USER = clef['email_host_user']
EMAIL_HOST_PASSWORD = clef['email_host_pass']
EMAIL_USE_TLS = True

if dev_settings():
    from .dev import *
else:
    from .prod import *
