from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from order_management.models import Order
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics  import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.mixins import *
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ModelViewSet


class OrderListView(ListView):
    model = Order
    queryset = Order.objects.all()
    template_name = "order_list.html"
    context_object_name = "my_order_list"

    # def get_queryset(self) -> QuerySet[Any]:
    #     return Order.objects.all()


class APIView(APIView):
    def get(self, request, *args, **kwargs):
        return Response(data={'name': "Mohit",})
    
class OrderListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        # data = []
        # for order in orders:
        #     data.append({
        #         "id": order.id,
        #         "name": order.name,
        #         "address": order.address,
        #     })
        data = orders.values()
        return Response(data=data,)
    
    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response(data={'name': "Mohit",})
    


class GetOrderView(APIView):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        order = Order.objects.get(**kwargs)
        # data = []
        # for order in orders:
        #     data.append({
        #         "id": order.id,
        #         "name": order.name,
        #         "address": order.address,
        #     })
        data = {
                "id": order.id,
                "name": order.name,
                "address": order.address,
        }
        return Response(data=data,)



class OrderListSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("name",)




class OrderCreateSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ("name", "address")
    
    def validate_name(self, data):
        if data == "Mohit":
            raise ValidationError("Name cannot be mohit")
        return data


class OrderListKaView(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

class OrderRetrieveView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    lookup_url_kwarg = 'id'

class OrderCreateView(CreateAPIView):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()


class OrderViewSet(ModelViewSet):
    serializer_class = OrderCreateSerializer
    queryset = Order.objects.all()
