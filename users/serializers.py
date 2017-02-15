# -*- coding: utf-8 -*-
import datetime
import json
from datetime import date
from django.contrib.auth import update_session_auth_hash
# from django.db.models import Q
from django.utils import timezone
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator
from users.models import User, UserMedia

class UserMediaSerializer(serializers.ModelSerializer):

	class Meta:
		model = UserMedia
		fields = ('id', 'user', 'user_media_file', 'user_media_file_created', 'user_profile')

class UserSerializer(serializers.ModelSerializer):
    # email = serializers.CharField(required=False, allow_blank=True, validators=[
    # UniqueValidator(
    #     queryset=User.objects.all(),
    #     message="My custom error",)])
    # is_active = serializers.BooleanField(required=False)
    user_media = UserMediaSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'is_active', 'is_admin', 'is_staff', 'username', 'first_name', 'last_name', 'user_created', 'user_updated', 'user_media',)
        read_only_fields = ('id', 'user_created', 'is_admin',)

    # def create(self, validated_data):
    #     cur_user = validated_data.pop('user')
    #     try:  
    #         user = User.objects.create_user(**validated_data)
    #         user.save()

    #         if cur_user.id:
    #             user.user_created_by = cur_user
    #         else:
    #             user.user_created_by = user

    #         user.save()
    #         send_basic_email.delay(user.id, 'CRE')

    #         return user
    #     except Exception, e:
    #         return Response({
    #             'status': 'Bad request',
    #             'message': 'Account could not be created with received data.'
    #         }, status=status.HTTP_400_BAD_REQUEST)

    # def update(self, instance, validated_data):
    #     instance.first_name = validated_data.get('first_name', instance.first_name)
    #     instance.last_name = validated_data.get('last_name', instance.last_name)
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.play_level = validated_data.get('play_level', instance.play_level)
    #     instance.user_pic = validated_data.get('user_pic', instance.user_pic)
    #     instance.user_credit = validated_data.get('user_credit', instance.user_credit)
    #     instance.recurring_credit = validated_data.get('recurring_credit', instance.recurring_credit)
    #     instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)        
    #     instance.user_updated_by = validated_data.pop('user')

    #     if validated_data.get('is_active') == 'true':
    #         if instance.is_active == False:
    #             send_basic_email.delay(instance.id, 'ACT')
    #         instance.is_active = True
    #     else:
    #         instance.is_active = False

    #     if instance.location and instance.location.id == validated_data.get('location[id]'):
    #             instance.location = validated_data.get('location', instance.location)
    #     elif 'location[id]' in validated_data:
    #         location_id = validated_data.get('location[id]')
    #         location = Location.objects.get(id=location_id)
    #         instance.location = location

    #     instance.save()
    #     password = validated_data.get('password', None)
    #     confirm_password = validated_data.get('confirm_password', None)

    #     if password and confirm_password and password == confirm_password:
    #         instance.set_password(password)
    #         instance.save()

    #         update_session_auth_hash(self.context.get('request'), instance)

    #     return instance

