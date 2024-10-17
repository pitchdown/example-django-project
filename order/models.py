from django.db import models


# Create your models here.
class UserCart(models.Model):
    user = models.OneToOneField("user.User", on_delete=models.CASCADE)