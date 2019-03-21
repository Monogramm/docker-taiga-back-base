# Importing common provides default settings, see:
# https://github.com/taigaio/taiga-back/blob/master/settings/common.py
from .common import *

#########################################
## GENERIC
#########################################

if os.getenv('TAIGA_DEBUG').lower() == 'true':
    DEBUG = True
else:
    DEBUG = False

if os.getenv('TAIGA_TEMPLATE_DEBUG').lower() == 'true':
    TEMPLATE_DEBUG = True
else:
    TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('TAIGA_DB_NAME'),
        'HOST': os.getenv('TAIGA_DB_HOST'),
        'USER': os.getenv('TAIGA_DB_USER'),
        'PASSWORD': os.getenv('TAIGA_DB_PASSWORD')
    }
}

TAIGA_HOSTNAME = os.getenv('TAIGA_HOSTNAME')

SITES['api']['domain'] = TAIGA_HOSTNAME
SITES['front']['domain'] = TAIGA_HOSTNAME

MEDIA_URL  = 'http://' + TAIGA_HOSTNAME + '/media/'
STATIC_URL = 'http://' + TAIGA_HOSTNAME + '/static/'


#########################################
## MAIL SYSTEM SETTINGS
#########################################

if os.getenv('TAIGA_ENABLE_EMAIL').lower() == 'true':
    DEFAULT_FROM_EMAIL = os.getenv('TAIGA_EMAIL_FROM')
    CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300 # in seconds

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    if os.getenv('TAIGA_EMAIL_USE_TLS').lower() == 'true':
        EMAIL_USE_TLS = True
    else:
        EMAIL_USE_TLS = False

    EMAIL_HOST = os.getenv('TAIGA_EMAIL_HOST')
    EMAIL_PORT = int(os.getenv('TAIGA_EMAIL_PORT'))
    EMAIL_HOST_USER = os.getenv('TAIGA_EMAIL_USER')
    EMAIL_HOST_PASSWORD = os.getenv('TAIGA_EMAIL_PASS')


#########################################
## SECURITY SETTINGS
#########################################

if os.getenv('TAIGA_SSL').lower() == 'true' or os.getenv('TAIGA_SSL_BY_REVERSE_PROXY').lower() == 'true':
    SITES['api']['scheme'] = 'https'
    SITES['front']['scheme'] = 'https'

    MEDIA_URL  = 'https://' + TAIGA_HOSTNAME + '/media/'
    STATIC_URL = 'https://' + TAIGA_HOSTNAME + '/static/'

SECRET_KEY = os.getenv('TAIGA_SECRET_KEY')


#########################################
## REGISTRATION
#########################################

if os.getenv('TAIGA_PUBLIC_REGISTER_ENABLED').lower() == 'true':
    PUBLIC_REGISTER_ENABLED = True
else:
    PUBLIC_REGISTER_ENABLED = False

# LIMIT ALLOWED DOMAINS FOR REGISTER AND INVITE
# None or [] values in USER_EMAIL_ALLOWED_DOMAINS means allow any domain
#USER_EMAIL_ALLOWED_DOMAINS = None

# PUCLIC OR PRIVATE NUMBER OF PROJECT PER USER
#MAX_PRIVATE_PROJECTS_PER_USER = None # None == no limit
#MAX_PUBLIC_PROJECTS_PER_USER = None # None == no limit
#MAX_MEMBERSHIPS_PRIVATE_PROJECTS = None # None == no limit
#MAX_MEMBERSHIPS_PUBLIC_PROJECTS = None # None == no limit


#########################################
## SITEMAP
#########################################

# If is True /front/sitemap.xml show a valid sitemap of taiga-front client
if os.getenv('TAIGA_SITEMAP_ENABLED').lower() == 'true':
    FRONT_SITEMAP_ENABLED = True
    FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second
else:
    FRONT_SITEMAP_ENABLED = False


#########################################
## FEEDBACK
#########################################

# Note: See config in taiga-front too
if os.getenv('TAIGA_FEEDBACK_ENABLED').lower() == 'true':
    FEEDBACK_ENABLED = True
    FEEDBACK_EMAIL = os.getenv('TAIGA_FEEDBACK_EMAIL')
else:
    FEEDBACK_ENABLED = False


#########################################
## STATS
#########################################

if os.getenv('TAIGA_STATS_ENABLED').lower() == 'true':
    STATS_ENABLED = True
    FRONT_SITEMAP_CACHE_TIMEOUT = 60*60  # In second
else:
    STATS_ENABLED = False


#########################################
## IMPORTERS
#########################################

# Configuration for the GitHub importer
# Remember to enable it in the front client too.
if os.getenv('TAIGA_IMPORTER_GITHUB_ENABLED').lower() == 'true':
    IMPORTERS["github"] = {
        "active": True, # Enable or disable the importer
        "client_id": os.getenv('TAIGA_IMPORTER_GITHUB_CLIENT_ID'),
        "client_secret": os.getenv('TAIGA_IMPORTER_GITHUB_CLIENT_SECRET')
    }


# Configuration for the Trello importer
# Remember to enable it in the front client too.
if os.getenv('TAIGA_IMPORTER_TRELLO_ENABLED').lower() == 'true':
    IMPORTERS["trello"] = {
        "active": True, # Enable or disable the importer
        "api_key": os.getenv('TAIGA_IMPORTER_TRELLO_API_KEY'),
        "secret_key": os.getenv('TAIGA_IMPORTER_TRELLO_API_SECRET')
    }


# Configuration for the Jira importer
# Remember to enable it in the front client too.
if os.getenv('TAIGA_IMPORTER_JIRA_ENABLED').lower() == 'true':
    IMPORTERS["jira"] = {
        "active": True, # Enable or disable the importer
        "consumer_key": os.getenv('TAIGA_IMPORTER_JIRA_CONSUMER_KEY'),
        "cert": os.getenv('TAIGA_IMPORTER_JIRA_CERT'),
        "pub_cert": os.getenv('TAIGA_IMPORTER_JIRA_PUB_CERT')
    }


# Configuration for the Asane importer
# Remember to enable it in the front client too.
if os.getenv('TAIGA_IMPORTER_ASANA_ENABLED').lower() == 'true':
    IMPORTERS["asana"] = {
        "active": True, # Enable or disable the importer
        "callback_url": "{}://{}/project/new/import/asana".format(SITES["front"]["scheme"],
                                                                  SITES["front"]["domain"]),
        "app_id": os.getenv('TAIGA_IMPORTER_ASANA_APP_ID'),
        "app_secret": os.getenv('TAIGA_IMPORTER_ASANA_APP_SECRET')
    }


#########################################
## EVENTS SETTINGS
#########################################

if os.getenv('RABBIT_HOST') is not None and os.getenv('REDIS_HOST') is not None:
    from .celery import *

    BROKER_URL = 'amqp://' + os.getenv('RABBIT_USER') + ':' + os.getenv('RABBIT_PASSWORD') + '@' + os.getenv('RABBIT_HOST') + ':' + os.getenv('RABBIT_PORT')
    CELERY_RESULT_BACKEND = 'redis://' + os.getenv('REDIS_HOST') + ':' + os.getenv('REDIS_PORT') + '/0'
    # Set to True to enable celery and work in async mode or False
    # to disable it and work in sync mode. You can find the celery
    # settings in settings/celery.py and settings/celery-local.py
    CELERY_ENABLED = True

    EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
    EVENTS_PUSH_BACKEND_OPTIONS = {"url": "amqp://" + os.getenv('RABBIT_USER') + ":" + os.getenv('RABBIT_PASSWORD') + "@" + os.getenv('RABBIT_HOST') + ":" + os.getenv('RABBIT_PORT') + "//"}

