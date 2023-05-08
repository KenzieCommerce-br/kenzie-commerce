from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework_simplejwt import authentication
from rest_framework import generics, permissions, response

from order_seller.models import OrderSeller
from products.models import Product
from users.models import User
from .models import Order

from .serializers import OrderSerializer, OrderDetailSerializer
from users.permissions import IsOwnerOnlyOrAdmin
from .permissions import IsClientOwnerOrAdmin


class OrderView(generics.ListCreateAPIView):

    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsClientOwnerOrAdmin]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):

        user = get_object_or_404(User, pk=self.kwargs['user_id'])
        serializer.save(user=user)

    def list(self, request, *args, **kwargs):

        queryset = get_list_or_404(Order, user_id=self.kwargs['user_id'])
        user = get_object_or_404(User, pk=self.kwargs['user_id'])

        if request.user == user or request.user.is_admin:
            page = self.paginate_queryset(queryset)

            if page is not None:

                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(queryset, many=True)
            return response.Response(serializer.data)

        else:
            return response.Response({'error': 'Request not authorized. ID User conflicted with route id.'})


class OrderDetailView(generics.ListAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer

    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [IsOwnerOnlyOrAdmin]

    def list(self, request, *args, **kwargs):

        queryset = get_list_or_404(Order, user_id=self.kwargs['user_id'])
        user = get_object_or_404(User, pk=self.kwargs['user_id'])

        if request.user == user or request.user.is_admin:

            list_orders = []
            list_products = []

            for order in queryset:
                list_orders.append(OrderSeller.objects.get(order_id=order.id))

            for order in list_orders:
                list_products.append(Product.objects.get(id=order.product_id))

            page = self.paginate_queryset(list_products)

            if page is not None:

                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(list_products, many=True)
            return response.Response(serializer.data)

        else:
            return response.Response({'error': 'Request not authorized. ID User conflicted with route id.'})
