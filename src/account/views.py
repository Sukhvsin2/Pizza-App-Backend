from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.models import User, update_last_login
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import json

class RegisterView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        # firstname = request.data['firstname']
        # lastname = request.data['lastname']
        user = User(username=username)
        # user.first_name(firstname)
        # user.last_name(lastname)
        user.set_password(password)
        # refresh = RefreshToken.for_user(user)
        user.save()
        return Response({'message': 'User Created'}, status=status.HTTP_200_OK)

class LoginView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user_exist = User.objects.filter(username=username).exists()
        if user_exist:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                update_last_login(None, user)
                token = RefreshToken.for_user(user)
                print(token)
                return Response({'token': str(token)},status=status.HTTP_200_OK)
            else:
                return Response({'message': 'username or password incorrect'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'User doesn\'t exist'}, status=status.HTTP_404_NOT_FOUND)