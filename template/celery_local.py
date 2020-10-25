# -*- coding: utf-8 -*-

from .celery import *

import os

broker_url = 'amqp://' + os.getenv('RABBIT_USER', 'guest') + ':' + os.getenv('RABBIT_PASSWORD', 'guest') + '@' + os.getenv('RABBIT_HOST', 'localhost') + ':' + os.getenv('RABBIT_PORT', '5672') + '//'
result_backend = 'redis://' + os.getenv('REDIS_HOST', 'localhost') + ':' + os.getenv('REDIS_PORT', '6379') + '/0'

timezone = os.getenv('TAIGA_TIMEZONE', 'Europe/Madrid')

if os.getenv('TAIGA_DEBUG').lower() == 'true':
    print("Taiga debug enabled", file=sys.stderr)
    DEBUG = True
else:
    DEBUG = False
