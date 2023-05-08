from django.db import models


class OrderOptions(models.TextChoices):

    ORDER_PLACED = 'PEDIDO REALIZADO'
    IN_PROGRESS = 'EM ANDAMENTO'
    DELIVERED = 'ENTREGUE'


class Order(models.Model):

    status = models.CharField(
        null=False, choices=OrderOptions.choices, default=OrderOptions.ORDER_PLACED
    )

    hour = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(
        'users.User', on_delete=models.CASCADE, related_name='orders'
    )

    def __rep__(self):
        return f'<Order ({self.id})>'
