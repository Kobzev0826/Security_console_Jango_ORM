import os
# from dotenv import load_dotenv
# load_dotenv()
from environs import Env
env = Env()
env.read_env()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': env('DB_HOST'),#os.getenv('DB_HOST'),
        'PORT': env('DB_PORT'),#os.getenv('DB_PORT'),
        'NAME': env('DB_NAME'),#os.getenv('DB_NAME'),
        'USER': env('DB_USER'),#os.getenv('DB_USER'),
        'PASSWORD': env('DB_PASSWORD')#os.getenv('DB_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env('DB_SECRET_KEY')#os.getenv('REPLACE_ME')

DEBUG = env.bool('DEBUG')#True

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
