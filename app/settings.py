import os

THIS_PATH = os.path.dirname(__file__)
PROJECT_PATH = os.path.abspath(os.path.join(THIS_PATH, os.pardir))


class Path:
    TEMPLATE_FOLDER = os.path.join(PROJECT_PATH, 'templates')
    STATIC_FOLDER = os.path.join(PROJECT_PATH, 'static')
    MEDIA_FOLDER = os.path.join(PROJECT_PATH, 'media')


class Settings(Path):
    SQLALCHEMY_ECHO = DEBUG = TESTING = False
    PROJECT_PATH = PROJECT_PATH
    REDIRECT_CODE = 301
    SECRET_KEY = '899b40167427672dda5b02206f1ffd6cee35b7aa10b9b'
    SECURITY_PASSWORD_SALT = '899b40167427672dda5b02206f1ffd6cee35b7aa10b9b'

    # Admin
    ADMIN_TEMPLATES = 'admin'
    ADMIN_KWARGS = {
        'name': 'Admin',
        'base_template': '/'.join((ADMIN_TEMPLATES, 'admin_base.html')),
        'template_mode': 'bootstrap3',
    }

    LOG_FILE = os.path.expanduser('~/log/app.log')


class Production(Settings):
    # Change values for production
    SQLALCHEMY_DATABASE_URI = (
        '{engine}://{auth_user}:{auth_passwd}@{url}/{name}'.format(
            engine='postgresql',
            name='app',
            url='localhost',
            auth_user='user',
            auth_passwd='123456',
        )
    )
    DEBUG=True


class Development(Settings):
    SQLALCHEMY_DATABASE_URI = 'postgresql:////drinke'
    #SQLALCHEMY_DATABASE_URI = (
    #    '{engine}://{auth_user}:{auth_passwd}@{url}/{name}'.format(
    #        engine='postgresql',
    #        name='app',
    #        url='localhost',
    #        auth_user='user',
    #        auth_passwd='123456',
    #    )
    #)
    SQLALCHEMY_ECHO = False
    DEBUG = TESTING = True
    REDURECT_CODE = 302

