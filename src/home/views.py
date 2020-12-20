from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import *
from .serializer import *

class HomeView(APIView):
    def get(self, request):
        queryset = Pizza.objects.all()
        serializer = PizzaSerializer(queryset, many=True)
        if serializer.is_valid:
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error_messages, status=status.HTTP_200_OK)


class OrderPizza(APIView):
    def post(self, request):
        user = request.user
        data = json.loads(request.body)
        try:
            pizza = Pizza.objects.get(id=data.get('id'))
            order = Order(user=user, pizza=pizza, amount=pizza.amount)
            order.save()
            return Response({'message': pizza.name + ' ordered!'})
        except Pizza.DoesNotExist:
            return Response({'error': 'Pizza Doesn\'t exist'})