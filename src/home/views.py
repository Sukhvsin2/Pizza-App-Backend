from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializer import *
from rest_framework.permissions import IsAuthenticated
import json


class HomeView(APIView):
    def get(self, request):
        queryset = Pizza.objects.all()
        serializer = PizzaSerializer(queryset, many=True)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_200_OK)


class OrderPizza(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        print(user.id)
        queryset = Order.objects.filter(user=user.id)
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user
        data = json.loads(request.body)
        try:
            pizza = Pizza.objects.get(id=data.get('id'))
            print(pizza.price)
            order = Order(user=user, pizza=pizza, amount=pizza.price)
            order.save()
            return Response({'message': pizza.name + ' ordered!'})
        except Pizza.DoesNotExist:
            return Response({'error': 'Pizza Doesn\'t exist'})