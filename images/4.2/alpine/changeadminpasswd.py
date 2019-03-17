import os
from django.apps import apps

user_model = apps.get_model('users', 'User')
u = user_model.objects.get(username = 'admin')
u.set_password(os.environ['TAIGA_ADMIN_PASSWORD'])
u.save()
