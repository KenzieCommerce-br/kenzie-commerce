from django.db import models


class Cart(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    products = models.ManyToManyField(
        "products.Product", through="CartItem", related_name="carts"
    )
    total_value = models.DecimalField(max_digits=8, decimal_places=2, null=True)


class CartItem(models.Model):
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
