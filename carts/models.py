from django.db import models


class Cart(models.Model):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    total_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    @property
    def total_value(self):
        total = 0
        for item in self.items.all():
            total += item.quantity * item.product.price
        return total

    def update_total_value(self):
        self.total_value = self.total_value
        self.save()


class CartItem(models.Model):
    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
    )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name="items")
    quantity = models.PositiveIntegerField(default=1)
