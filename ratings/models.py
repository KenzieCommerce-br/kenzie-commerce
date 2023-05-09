from django.db import models


class RatingChoices(models.IntegerChoices):
    HATED = 1
    DID_NOT_LIKE = 2
    INDIFFERENT = 3
    LIKED = 4
    LOVED = 5


class Rating(models.Model):

    comments = models.CharField(max_length=250)
    stars = models.CharField(choices=RatingChoices.choices, default=RatingChoices.LOVED)

    order = models.ForeignKey(
        'orders.Order',
        on_delete=models.CASCADE,
        related_name='order_ratings',
        null=False
    )

    product = models.ForeignKey(
        'products.Product',
        on_delete=models.CASCADE,
        related_name='product_rating',
        null=False
    )

    user = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        related_name='user_rating'
    )
