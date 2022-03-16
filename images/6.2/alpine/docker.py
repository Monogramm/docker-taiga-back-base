# Importing common provides default settings, see:
# https://github.com/taigaio/taiga-back/blob/master/settings/common.py
from .common import *
import os, sys

#########################################
## GENERIC
#########################################

if os.getenv('TAIGA_DEBUG').lower() == 'true':
    print("Taiga debug enabled", file=sys.stderr)
    DEBUG = True
else:
    DEBUG = False

if os.getenv('TAIGA_TEMPLATE_DEBUG').lower() == 'true':
    print("Taiga template debug enabled", file=sys.stderr)
    TEMPLATE_DEBUG = True
else:
    TEMPLATE_DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('TAIGA_DB_NAME', os.getenv('POSTGRES_DB')),
        'HOST': os.getenv('TAIGA_DB_HOST', os.getenv('POSTGRES_HOST')),
        'PORT': os.getenv('TAIGA_DB_PORT', os.getenv('POSTGRES_PORT','5432')),
        'USER': os.getenv('TAIGA_DB_USER', os.getenv('POSTGRES_USER')),
        'PASSWORD': os.getenv('TAIGA_DB_PASSWORD', os.getenv('POSTGRES_PASSWORD'))
    }
}

TAIGA_HOSTNAME = os.getenv('TAIGA_HOSTNAME', os.getenv('TAIGA_SITES_DOMAIN'))

SITES['api']['domain'] = TAIGA_HOSTNAME
SITES['front']['domain'] = TAIGA_HOSTNAME

INSTANCE_TYPE = "D"

WEBHOOKS_ENABLED = True

# Setting DEFAULT_PROJECT_SLUG_PREFIX to false
# removes the username from project slug
DEFAULT_PROJECT_SLUG_PREFIX = os.getenv('DEFAULT_PROJECT_SLUG_PREFIX', 'False').lower() == 'true'


#########################################
## MAIL SYSTEM SETTINGS
#########################################

if os.getenv('TAIGA_ENABLE_EMAIL', os.getenv('ENABLE_EMAIL', 'False')).lower() == 'true':
    print("Enabling Taiga emails...", file=sys.stderr)
    DEFAULT_FROM_EMAIL = os.getenv('TAIGA_EMAIL_FROM', os.getenv('DEFAULT_FROM_EMAIL'))
    CHANGE_NOTIFICATIONS_MIN_INTERVAL = int(os.getenv('TAIGA_NOTIFICATIONS_INTERVAL', '120')) # in seconds

    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

    EMAIL_USE_TLS = os.getenv('TAIGA_EMAIL_USE_TLS', os.getenv('EMAIL_USE_TLS', 'False')).lower() == 'true'
    EMAIL_USE_SSL = os.getenv('TAIGA_EMAIL_USE_SSL', os.getenv('EMAIL_USE_SSL', 'False')).lower() == 'true'

    EMAIL_HOST = os.getenv('TAIGA_EMAIL_HOST', os.getenv('EMAIL_HOST'))
    EMAIL_PORT = int(os.getenv('TAIGA_EMAIL_PORT', os.getenv('EMAIL_PORT', '587')))
    EMAIL_HOST_USER = os.getenv('TAIGA_EMAIL_USER', os.getenv('EMAIL_HOST_USER'))
    EMAIL_HOST_PASSWORD = os.getenv('TAIGA_EMAIL_PASS', os.getenv('EMAIL_HOST_PASSWORD'))


#########################################
## SESSION
#########################################

SESSION_COOKIE_SECURE = os.getenv('SESSION_COOKIE_SECURE', 'True').lower() == 'true'
CSRF_COOKIE_SECURE = os.getenv('CSRF_COOKIE_SECURE', 'True').lower() == 'true'


#########################################
## SECURITY SETTINGS
#########################################

if os.getenv('TAIGA_SSL').lower() == 'true' or os.getenv('TAIGA_SSL_BY_REVERSE_PROXY').lower() == 'true':
    print("Enabling Taiga SSL...", file=sys.stderr)
    SITES['api']['scheme'] = 'https'
    SITES['front']['scheme'] = 'https'

    TAIGA_URL  = 'https://' + TAIGA_HOSTNAME
    MEDIA_URL  = TAIGA_URL + '/media/'
    STATIC_URL = TAIGA_URL + '/static/'
else:
    SITES['api']['scheme'] = 'http'
    SITES['front']['scheme'] = 'http'

    TAIGA_URL  = 'http://' + TAIGA_HOSTNAME
    MEDIA_URL  = TAIGA_URL + '/media/'
    STATIC_URL = TAIGA_URL + '/static/'


SECRET_KEY = os.getenv('TAIGA_SECRET_KEY')


#########################################
## REGISTRATION
#########################################

if os.getenv('TAIGA_PUBLIC_REGISTER_ENABLED', os.getenv('PUBLIC_REGISTER_ENABLED', 'False')).lower() == 'true':
    print("Taiga registration enabled", file=sys.stderr)
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
if os.getenv('TAIGA_SITEMAP_ENABLED', os.getenv('FRONT_SITEMAP_ENABLED', 'False')).lower() == 'true':
    print("Taiga sitemap enabled", file=sys.stderr)
    FRONT_SITEMAP_ENABLED = True
    FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second
else:
    FRONT_SITEMAP_ENABLED = False


#########################################
## FEEDBACK
#########################################

# Note: See config in taiga-front too
if os.getenv('TAIGA_FEEDBACK_ENABLED', os.getenv('FEEDBACK_ENABLED', 'False')).lower() == 'true':
    print("Taiga feedback enabled", file=sys.stderr)
    FEEDBACK_ENABLED = True
    FEEDBACK_EMAIL = os.getenv('TAIGA_FEEDBACK_EMAIL', os.getenv('FEEDBACK_EMAIL'))
else:
    FEEDBACK_ENABLED = False


#########################################
## STATS
#########################################

if os.getenv('TAIGA_STATS_ENABLED', os.getenv('STATS_ENABLED', 'False')).lower() == 'true':
    print("Taiga statistics enabled", file=sys.stderr)
    STATS_ENABLED = True
else:
    STATS_ENABLED = False


#########################################
## TELEMETRY
#########################################

if os.getenv('TAIGA_TELEMETRY_ENABLED', os.getenv('ENABLE_TELEMETRY')).lower() == 'true':
    print("Taiga anonymous telemetry enabled", file=sys.stderr)
    ENABLE_TELEMETRY = True
else:
    ENABLE_TELEMETRY = False


#########################################
## IMPORTERS
#########################################

# Configuration for the GitHub importer
# Remember to enable it in the front client too.
if os.getenv('TAIGA_IMPORTER_GITHUB_ENABLED', os.getenv('ENABLE_GITHUB_IMPORTER', 'False')).lower() == 'true':
    print("Taiga github importer enabled", file=sys.stderr)
    IMPORTERS["github"] = {
        "active": True, # Enable or disable the importer
        "client_id": os.getenv('TAIGA_IMPORTER_GITHUB_CLIENT_ID', os.getenv('GITHUB_IMPORTER_CLIENT_ID')),
        "client_secret": os.getenv('TAIGA_IMPORTER_GITHUB_CLIENT_SECRET', os.getenv('GITHUB_IMPORTER_CLIENT_SECRET'))
    }


# Configuration for the Trello importer
# Remember to enable it in the front client too.
if os.getenv('TAIGA_IMPORTER_TRELLO_ENABLED', os.getenv('ENABLE_TRELLO_IMPORTER', 'False')).lower() == 'true':
    print("Taiga trello importer enabled", file=sys.stderr)
    IMPORTERS["trello"] = {
        "active": True, # Enable or disable the importer
        "api_key": os.getenv('TAIGA_IMPORTER_TRELLO_API_KEY', os.getenv('TRELLO_IMPORTER_API_KEY')),
        "secret_key": os.getenv('TAIGA_IMPORTER_TRELLO_API_SECRET', os.getenv('TRELLO_IMPORTER_SECRET_KEY'))
    }


# Configuration for the Jira importer
# Remember to enable it in the front client too.
if os.getenv('TAIGA_IMPORTER_JIRA_ENABLED', os.getenv('ENABLE_JIRA_IMPORTER', 'False')).lower() == 'true':
    print("Taiga jira importer enabled", file=sys.stderr)
    IMPORTERS["jira"] = {
        "active": True, # Enable or disable the importer
        "consumer_key": os.getenv('TAIGA_IMPORTER_JIRA_CONSUMER_KEY', os.getenv('JIRA_IMPORTER_CONSUMER_KEY')),
        "cert": os.getenv('TAIGA_IMPORTER_JIRA_CERT', os.getenv('JIRA_IMPORTER_CERT')),
        "pub_cert": os.getenv('TAIGA_IMPORTER_JIRA_PUB_CERT', os.getenv('JIRA_IMPORTER_PUB_CERT'))
    }


# Configuration for the Asane importer
# Remember to enable it in the front client too.
if os.getenv('TAIGA_IMPORTER_ASANA_ENABLED', os.getenv('ENABLE_ASANA_IMPORTER', 'False')).lower() == 'true':
    print("Taiga asana importer enabled", file=sys.stderr)
    IMPORTERS["asana"] = {
        "active": True, # Enable or disable the importer
        "callback_url": "{}://{}/project/new/import/asana".format(SITES["front"]["scheme"],
                                                                  SITES["front"]["domain"]),
        "app_id": os.getenv('TAIGA_IMPORTER_ASANA_APP_ID', os.getenv('ASANA_IMPORTER_APP_ID')),
        "app_secret": os.getenv('TAIGA_IMPORTER_ASANA_APP_SECRET', os.getenv('ASANA_IMPORTER_APP_SECRET'))
    }


#########################################
## EVENTS/ASYNC SETTINGS
#########################################

if os.getenv('TAIGA_EVENTS_ENABLED', os.getenv('EVENTS_ENABLED', 'False')).lower() == 'true':
    print("Taiga events enabled", file=sys.stderr)
    broker_url = 'amqp://' + os.getenv('RABBIT_USER', os.getenv('RABBITMQ_USER', 'guest')) + ':' + os.getenv('RABBIT_PASSWORD', os.getenv('RABBITMQ_PASS', 'guest')) + '@' + os.getenv('RABBIT_HOST', os.getenv('RABBITMQ_HOST', 'localhost')) + ':' + os.getenv('RABBIT_PORT', os.getenv('RABBITMQ_PORT', '5672')) + os.getenv('RABBIT_VHOST', os.getenv('RABBITMQ_VHOST', '/'))

    EVENTS_PUSH_BACKEND_URL = broker_url
    EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
    EVENTS_PUSH_BACKEND_OPTIONS = {"url": EVENTS_PUSH_BACKEND_URL}

if os.getenv('TAIGA_ASYNC_ENABLED', os.getenv('CELERY_ENABLED', 'False')).lower() == 'true':
    print("Taiga async mode enabled", file=sys.stderr)

    # Not present in Taiga 6+
    #from .celery import *

    broker_url = 'amqp://' + os.getenv('RABBIT_USER', os.getenv('RABBITMQ_USER', 'guest')) + ':' + os.getenv('RABBIT_PASSWORD', os.getenv('RABBITMQ_PASS', 'guest')) + '@' + os.getenv('RABBIT_HOST', os.getenv('RABBITMQ_HOST', 'localhost')) + ':' + os.getenv('RABBIT_PORT', os.getenv('RABBITMQ_PORT', '5672')) + os.getenv('RABBIT_VHOST', os.getenv('RABBITMQ_VHOST', '/'))
    result_backend = 'redis://' + os.getenv('REDIS_HOST', 'localhost') + ':' + os.getenv('REDIS_PORT', '6379') + '/0'

    timezone = os.getenv('TAIGA_TIMEZONE', 'Europe/Madrid')

    # Set to True to enable celery and work in async mode or False
    # to disable it and work in sync mode. You can find the celery
    # settings in settings/celery_local.py
    CELERY_ENABLED = True
    CELERY_BROKER_URL = broker_url
    CELERY_RESULT_BACKEND = result_backend

    # Only for Taiga 6+
    from kombu import Queue

    accept_content = ['pickle',] # Values are 'pickle', 'json', 'msgpack' and 'yaml'
    task_serializer = "pickle"
    result_serializer = "pickle"
    task_default_queue = 'tasks'
    task_queues = (
        Queue('tasks', routing_key='task.#'),
        Queue('transient', routing_key='transient.#', delivery_mode=1)
    )
    task_default_exchange = 'tasks'
    task_default_exchange_type = 'topic'
    task_default_routing_key = 'task.default'

    CELERY_ACCEPT_CONTENT = accept_content
    CELERY_TASK_SERIALIZER = task_serializer
    CELERY_RESULT_SERIALIZER = result_serializer
    CELERY_TIMEZONE = timezone
    CELERY_TASK_DEFAULT_QUEUE = task_default_queue
    CELERY_QUEUES = (
        Queue('tasks', routing_key='task.#'),
        Queue('transient', routing_key='transient.#', delivery_mode=1)
    )
    CELERY_TASK_DEFAULT_EXCHANGE = task_default_exchange
    CELERY_TASK_DEFAULT_EXCHANGE_TYPE = task_default_exchange_type
    CELERY_TASK_DEFAULT_ROUTING_KEY = task_default_routing_key
