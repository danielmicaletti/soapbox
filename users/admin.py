# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from users.models import User, UserMedia

class UserMediaAdmin(admin.ModelAdmin):

    class Meta:
        model = UserMedia

    list_display = ('user_media_created', 'user', 'user_media_file', 'user_profile',)
    list_filter = ('user_media_created', 'user', 'user_profile',)
    ordering = ('-user_media_created',)
    filter_horizontal = ()

admin.site.register(UserMedia, UserMediaAdmin)

class UserAdmin(admin.ModelAdmin):

    class Meta:
        model = User

    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'user_created',)
    list_filter = ('is_active', 'username', 'first_name', 'last_name', 'user_created', 'is_admin',)
    readonly_fields = ('user_created', 'user_updated', 'last_login',)

    fieldsets = (
        ('Authorization and Login info', {'fields': ('username', 'password',)}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email',)}),
        (None, {'fields': ('last_login', 'user_created_by', 'user_created', 'user_updated_by', 'user_updated',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active',)}),
    )

    add_fieldsets = (
        ('Authorization and Login info', {'fields': ('username', 'password1', 'password2')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email',)}),
        (None, {'fields': ('user_created_by', 'user_created', 'user_updated_by', 'user_updated',)}),
        ('Permissions', {'fields': ('is_admin', 'is_active',)}),
    )

    ordering = ('-user_created',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)