# Generated by Django 4.2 on 2023-05-08 14:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("addresses", "0002_alter_address_zip_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="zip_code",
            field=models.IntegerField(),
        ),
    ]