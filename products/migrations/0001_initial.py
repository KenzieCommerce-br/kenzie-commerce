# Generated by Django 4.2 on 2023-05-10 13:23

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
                ("price", models.FloatField()),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Teclado", "Teclado"),
                            ("Mouse", "Mouse"),
                            ("Notebook", "Notebook"),
                            ("HD", "Hd"),
                            ("Processador", "Processador"),
                            ("PlacaMãe", "Placamãe"),
                            ("Gabinete", "Gabinete"),
                            ("NN", "Nn"),
                        ],
                        default="NN",
                        max_length=20,
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        height_field=230,
                        upload_to=products.models.upload_image_product,
                        width_field=230,
                    ),
                ),
                ("stock", models.IntegerField()),
                ("available", models.BooleanField(default=True)),
            ],
        ),
    ]
