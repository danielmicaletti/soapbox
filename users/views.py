# -*- coding: utf-8 -*-
import json
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
# from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.utils import timezone
from io import BytesIO
from rest_framework import permissions, status, views, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser, MultiPartParser, FormParser, FileUploadParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework_jwt.settings import api_settings
from users.models import User, UserMedia
from users.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JSONWebTokenAuthentication,)

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)
        return (permissions.IsAuthenticated(),)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user, **self.request.data)
        else:
            return Response({
                'status': 'Bad request',
                'message': 'Account could not be created with received data.'
            }, status=status.HTTP_400_BAD_REQUEST)

    # def perform_update(self, serializer):
    #     if serializer.is_valid():
    #         temp_file = self.request.data.pop('user_pic')
    #         file_dict = {}
    #         for i in self.request.data:
    #             if i != 'user_pic': 
    #                 item = self.request.data[i]
    #                 file_dict[i] = item
    #         for f in temp_file:
    #             file_dict['user_pic'] = f

    #         serializer.save(user=self.request.user, **file_dict)

class LoginView(views.APIView):

    def post(self, request, format=None):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                serialized = UserSerializer(user)
                return Response(serialized.data)
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username or password invalid'
            }, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(views.APIView):

    def post(self, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)