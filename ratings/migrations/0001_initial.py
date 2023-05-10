# Generated by Django 4.2 on 2023-05-10 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("orders", "0001_initial"),
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Rating",
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
                ("comments", models.CharField(max_length=250)),
                (
                    "stars",
                    models.CharField(
                        choices=[
                            (1, "Hated"),
                            (2, "Did Not Like"),
                            (3, "Indifferent"),
                            (4, "Liked"),
                            (5, "Loved"),
                        ],
                        default=5,
                    ),
                ),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="order_ratings",
                        to="orders.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="product_rating",
                        to="products.product",
                    ),
                ),
            ],
        ),
    ]
