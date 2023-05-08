from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, response, status
from rest_framework_simplejwt import authentication
from .serializers import OrderSellerSerializer, OrderSellerStatusSerializer

from order_seller.models import OrderSeller
from orders.models import Order
from users.models import User


class OrderSellerView(generics.UpdateAPIView):

    queryset = Order.objects.all()
    serializer_class = OrderSellerSerializer
    lookup_url_kwarg = 'order_id'

    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return response.Response(
            {'email_sent_to:': instance.user.email, 'data': serializer.data},
            status=status.HTTP_200_OK,
        )

    def perform_update(self, serializer):
        order = get_object_or_404(Order, pk=self.kwargs['order_id'])
        serializer.save(order=order)


class OrderSellerPendingView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSellerStatusSerializer

    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):

        queryset = Order.objects.all()
        user = get_object_or_404(User, pk=self.kwargs['seller_id'])

        all_orders = []
        list_orders = []
        pending_orders = []

        if request.user == user or request.user.is_admin:

            all_orders.append(OrderSeller.objects.get(seller=user))
            for order in all_orders:
                list_orders = Order.objects.filter(id=order.id)

            for item in list_orders:
                if item.status != 'ENTREGUE':
                    pending_orders.append(item)

            page = self.paginate_queryset(pending_orders)

            if page is not None:

                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(pending_orders, many=True)
            return response.Response(serializer.data)

        else:
            return response.Response({'error': 'Request not authorized. ID User conflicted with route id.'})


class OrderSellerFinishedView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSellerStatusSerializer

    authentication_classes = [authentication.JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):

        queryset = Order.objects.all()
        user = get_object_or_404(User, pk=self.kwargs['seller_id'])

        all_orders = []
        list_orders = []
        pending_orders = []

        if request.user == user or request.user.is_admin:

            all_orders.append(OrderSeller.objects.get(seller=user))
            for order in all_orders:
                list_orders = Order.objects.filter(id=order.id)

            for item in list_orders:
                if item.status == 'ENTREGUE':
                    pending_orders.append(item)

            page = self.paginate_queryset(pending_orders)

            if page is not None:

                serializer = self.get_serializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            serializer = self.get_serializer(pending_orders, many=True)
            return response.Response(serializer.data)

        else:
            return response.Response({'error': 'Request not authorized. ID User conflicted with route id.'})
