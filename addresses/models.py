from django.db import models
from django.core.validators import MaxLengthValidator


class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=10)
    complement = models.CharField(max_length=100, null=True)
    zip_code = models.IntegerField(validators=[MaxLengthValidator(8)])

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="address",
    )

    def __rep__(self):
        return f"<Address ({self.id}) - {self.street}>"
