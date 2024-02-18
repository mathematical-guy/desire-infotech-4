from django.contrib import admin
from django.urls import path
from order_management.views import (OrderListView, APIView, OrderListAPIView, 
                                    GetOrderView, OrderListKaView, OrderRetrieveView,
                                    OrderCreateView, OrderViewSet
                                    )
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("main_order", OrderViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('order-list', OrderListView.as_view()),
    path('apiview', APIView.as_view()),
    path('orderlist', OrderListAPIView.as_view()),
    path('get_order/<int:id>', GetOrderView.as_view()),
    path('order_list_view', OrderListKaView.as_view()),
    path('order_retrieve_view/<int:id>', OrderRetrieveView.as_view()),
    path('order_create_view', OrderCreateView.as_view()),
]


urlpatterns += router.urls