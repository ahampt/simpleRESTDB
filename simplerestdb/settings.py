# Django settings for simplerestdb project.
import os
relpath = lambda *x: os.path.join(os.path.abspath(os.path.dirname(__file__)), *x)

VERSION = '1.0.0'

ENVIRONMENT = 'DEVELOPMENT'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ACCESS_PASSWORD = 'simple'

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'simplerestdb_db',
		'USER': 'root',
		'PASSWORD': 'root',
		'HOST': '',
		'PORT': '',
    }
}

TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

PREFIX_URL = ''

STATIC_ROOT = ''

STATIC_URL = '/' + PREFIX_URL + 'static/'

# Additional locations of static files
STATICFILES_DIRS = (
	relpath('static/'),
)

STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'f#*43i2i3d4z_$(oe7sfbg(ny_%%0%j9qujva0llr2)a7zim($'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.request',
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',
	'django.core.context_processors.static',
	'django.core.context_processors.tz',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
)

ROOT_URLCONF = 'webapp.urls'

# Python dotted path to the WSGI application used by Django's runserver.
#WSGI_APPLICATION = 'simplerestdb.wsgi.application'

TEMPLATE_DIRS = (
	relpath('webapp/templates/'),
)

INSTALLED_APPS = (
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.staticfiles',
	'webapp',
)

LOGGING_DIR = '/var/log/simplerestdb/'

LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'formatters': {
		'verbose': {
			'format': '%(levelname)s ' + 'v' + VERSION + ' %(asctime)s: %(message)s'
		}
	},
	'handlers': {
		'site': {
			'level': 'DEBUG',
			'class': 'logging.FileHandler',
			'formatter': 'verbose',
			'filename': LOGGING_DIR + 'site.log',
		},
		'database': {
			'level': 'DEBUG',
			'class': 'logging.FileHandler',
			'formatter': 'verbose',
			'filename': LOGGING_DIR + 'database.log'
		}
	},
	'loggers': {
		'log.site': {
			'handlers': ['site'],
			'level': 'DEBUG',
			'propagate': False,
		},
		'log.database': {
			'handlers': ['database'],
			'level': 'DEBUG',
			'propagate': False,
		}
	}
}
try:
	from local_settings import *
except ImportError:
	print 'Failed to load local settings'
