# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.core.files.storage import default_storage
from django.db import models
from django.utils.encoding import smart_unicode
from time import time

def get_upload_file_name(instance, filename):

    return settings.UPLOAD_FILE_PATTERN % (str(time()).replace('.','_'), filename)

class UserManager(BaseUserManager):

    def create_user(self, username, password=None, **kwargs):
        if not username:
            raise ValueError('Users must have a valid username.')

        # if not email:
        #     raise ValueError('Users must have a valid email.')

        user = self.model(
            username=username,
            first_name=kwargs.get('first_name'), last_name=kwargs.get('last_name'),
            email=kwargs.get('email'))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password, **kwargs):
        user = self.create_user(username=username, email=email, password=password)
        user.username = username
        user.email = email
        user.is_admin = True
        user.is_active = True
        user.save()

        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    user_created = models.DateTimeField(auto_now_add=True)
    user_created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='created_user', null=True, blank=True, unique=False)
    user_updated = models.DateTimeField(auto_now=True)
    user_updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='updated_user', null=True, blank=True, unique=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __unicode__(self):
        return smart_unicode(self.username)

    def get_full_name(self):
        return ' '.join([self.first_name, self.last_name])

    def get_short_name(self):
        return self.first_name

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin 

class UserMedia(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_media')
    user_media_file = models.FileField(upload_to=get_upload_file_name)
    user_media_created = models.DateTimeField(auto_now_add=True)
    user_profile = models.BooleanField(default=False)
