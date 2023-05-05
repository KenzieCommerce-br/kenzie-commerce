from django.db import models


class ProductCategories(models.TextChoices):
    Teclado = "Teclado"
    Mouse = "Mouse"
    Notebook = "Notebook"
    HD = "HD"
    Processador = "Processador"
    PlacaMãe = "PlacaMãe"
    Gabinete = "Gabinete"
    NN = "NN"


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    price = models.FloatField()
    category = models.CharField(
        max_length=20,
        choices=ProductCategories.choices,
        default=ProductCategories.NN,
    )
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="products"
    )
