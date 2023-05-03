from django.db import models


class ProductCategories(models.TextChoices):
    P = "P"
    M = "M"
    G = "G"
    D = "D"
    NN = "NN"


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    category = models.CharField(
        null=False,
        max_length=20,
        choices=ProductCategories.choices,
        default=ProductCategories.NN,
    )
    stock = models.IntegerField()
    avaliable = models.BooleanField(default=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="products"
    )
