from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, response, status
from rest_framework_simplejwt import authentication
from .serializers import OrderSellerSerializer
from orders.models import Order


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
