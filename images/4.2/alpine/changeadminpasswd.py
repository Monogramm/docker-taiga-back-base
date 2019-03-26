import os
from django.apps import apps

user_model = apps.get_model('users', 'User')

username_unique = 'admin'
email = 'admin@' + os.environ['TAIGA_HOSTNAME']
full_name = 'Taiga Admin'
superuser = True

try:
    user = user_model.objects.get(username = username_unique)
except user_model.DoesNotExist:
    print('Creating "' + username_unique + '" user with requested password')
    user = user_model.objects.create(username = username_unique,
                                        email = email,
                                        full_name = full_name,
                                        is_superuser = superuser)

    user.set_password(os.environ['TAIGA_ADMIN_PASSWORD'])
    user.save()
    print('User "' + username_unique + '" created with requested password')
else:
    print('Updating "' + username_unique + '" user with requested password')
    user.set_password(os.environ['TAIGA_ADMIN_PASSWORD'])
    user.save()
    print('User "' + username_unique + '" updated with requested password')
