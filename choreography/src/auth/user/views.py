from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


class RegisterAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        if User.objects.filter(username=username).exists():
            return Response({'message': "Username is already registered"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password)
        refresh_token, access_token = user.token

        return Response({
            'refresh': str(refresh_token),
            'access': str(access_token),
        },
            status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            refresh_token, access_token = user.token
            return Response({
                'refresh': str(refresh_token),
                'access': str(access_token),
            },
                status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Wrong password or username'}, status=status.HTTP_401_UNAUTHORIZED)


class ValidateTokenAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        return Response({'message': 'Token is valid'}, status=status.HTTP_200_OK)
