from django.db import models


class OrderSeller(models.Model):

    quantity = models.IntegerField()
    price = models.FloatField()

    product = models.OneToOneField(
        'products.Product', on_delete=models.CASCADE, related_name='order_seller'
    )

    seller = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='seller'
    )

    order = models.ForeignKey(
        'orders.Order', on_delete=models.CASCADE, related_name='seller'
    )

    def __repr__(self):
        return f'<OrderSeller ({self.id})>'
