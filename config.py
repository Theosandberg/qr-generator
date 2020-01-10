import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you_will_never_guess_hahaha'
    QRCODE_LOCATION = os.path.join(basedir, 'app/static/qrcodes')
