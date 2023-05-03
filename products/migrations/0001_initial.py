# Generated by Django 4.2 on 2023-05-02 16:39

from django.db import migrations, models


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
                            ("P", "P"),
                            ("M", "M"),
                            ("G", "G"),
                            ("D", "D"),
                            ("NN", "Nn"),
                        ],
                        default="NN",
                        max_length=20,
                    ),
                ),
                ("stock", models.IntegerField()),
                ("avaliable", models.BooleanField(default=True)),
            ],
        ),
    ]