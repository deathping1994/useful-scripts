from django.contrib import auth
from django.conf import settings
import os

"""
Creates super user with custom fields in django environment
"""

User = auth.get_user_model()

def createsuperuser():
    # env = raw_input("Enter environment (test/prod):")
    # if env == 'prod':
    #     # settings.configure(default_settings='saleor.settings')
    #     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saleor.settings")
    # else:
    #     settings.configure(default_settings='saleor.test_settings')
    #     # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "saleor.test_settings")

    email = raw_input("Enter Email:")
    mobile = raw_input('Enter mobile number:')
    password = 'test'
    check = ''

    while password != check:
        password = raw_input('Enter Password:')
        check = raw_input('Enter Password (again):')
    pharmacist = raw_input('is pharmacist ? (Y/N):')
    user = User.objects.create_user(email=email, password=password, mobile=mobile)

    user.is_superuser = True
    user.is_active = True
    user.is_staff = True
    if pharmacist == 'Y':
        user.is_pharmacist = True
    else:
        user.is_pharmacist = False
    user.save()
    print "User created successfully"

def run():
    createsuperuser()
