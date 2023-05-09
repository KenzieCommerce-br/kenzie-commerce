from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import response, status, permissions
from rest_framework.generics import ListCreateAPIView
from django.shortcuts import get_object_or_404

from .models import Rating
from users.models import User
from orders.models import Order
from products.models import Product
from order_seller.models import OrderSeller
from .serializers import RatingSerializer


class RatingView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = RatingSerializer
    queryset = OrderSeller.objects.all()
    lookup_url_kwarg = 'user_id'

    def get_queryset(self):

        queryset_order = Order.objects.all()
        queryset_order_seller = OrderSeller.objects.all()
        queryset_ratings = Rating.objects.all()

        user_id = self.kwargs['user_id']
        product_id = self.kwargs['product_id']

        product = get_object_or_404(Product, id=product_id)
        ensure_rating = queryset_ratings.filter(user_id=user_id, product_id=product_id)

        if user_id is not None and product_id is not None:

            list_pending = []
            list_finished = []

            orders = queryset_order.filter(user_id=user_id)
            order_sellers = queryset_order_seller.filter(product_id=product_id)

            for order in orders:
                if order.status != 'ENTREGUE':
                    list_pending.append(order)

                if order.status == 'ENTREGUE':
                    list_finished.append(order)

            return [list_pending, list_finished, order_sellers, product, ensure_rating]

    def create(self, request, *args, **kwargs):

        user = get_object_or_404(User, id=self.kwargs["user_id"])

        if request.user == user or request.user.is_admin:
            orders_user = self.get_queryset()

            if len(orders_user[4]) > 0:
                return response.Response({
                    'error': 'Você já avaliou este produto!'
                }, status=status.HTTP_400_BAD_REQUEST)

            # [0] -> não entregue, [1] -> entregue
            # [2] -> order_seller, [3] -> produto, [4] -> avaliação

            for order in orders_user[1]:

                if order.status == 'ENTREGUE':

                    for order_seller in orders_user[2]:

                        if order is not None and order_seller is not None:

                            if order_seller.product.id == self.kwargs['product_id']:

                                if order_seller.order_id == order.id:

                                    serializer = self.get_serializer(data=request.data)
                                    serializer.is_valid(raise_exception=True)

                                    serializer.save(user=user, order=order, product=order_seller.product)

                                    return response.Response(
                                        serializer.data, status=status.HTTP_201_CREATED
                                    )

                                else:
                                    return response.Response(
                                        {'message': 'A avaliação será liberada após a entrega do produto.'},
                                        status=status.HTTP_401_UNAUTHORIZED
                                    )
        else:
            return response.Response(
                {'error': 'Este usuário não está autorizado à acessar essa informação.'},
                status=status.HTTP_400_BAD_REQUEST
            )
