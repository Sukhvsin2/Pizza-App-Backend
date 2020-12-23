from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class RegisterView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User(username=username)
        user.set_password(password)
        refresh = RefreshToken.for_user(user)
        # refresh.set_exp(lifetime=datetime.timedelta(days=1))
        user.save()
        return Response({'message': 'User Created'}, status=status.HTTP_200_OK)

class LoginView(APIView):

    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        try:
            user = User.objects.get(username=username)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response({'message': 'username or password incorrect'}, status=status.HTTP_404_NOT_FOUND)
        # if user.DoesNotExist:
        #     print('chekc login')