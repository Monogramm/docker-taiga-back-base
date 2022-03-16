# -*- coding: utf-8 -*-

# Not present (or used) in Taiga 6+
from .celery import *

import os, sys

broker_url = 'amqp://' + os.getenv('RABBIT_USER', os.getenv('RABBITMQ_USER', 'guest')) + ':' + os.getenv('RABBIT_PASSWORD', os.getenv('RABBITMQ_PASS', 'guest')) + '@' + os.getenv('RABBIT_HOST', os.getenv('RABBITMQ_HOST', 'localhost')) + ':' + os.getenv('RABBIT_PORT', os.getenv('RABBITMQ_PORT', '5672')) + os.getenv('RABBIT_VHOST', os.getenv('RABBITMQ_VHOST', '/'))
result_backend = 'redis://' + os.getenv('REDIS_HOST', 'localhost') + ':' + os.getenv('REDIS_PORT', '6379') + '/0'

timezone = os.getenv('TAIGA_TIMEZONE', 'Europe/Madrid')

if os.getenv('TAIGA_DEBUG').lower() == 'true':
    print("Taiga debug enabled", file=sys.stderr)
    DEBUG = True
else:
    DEBUG = False
