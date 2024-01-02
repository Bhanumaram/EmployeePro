from django.db import models

# Create your models here.
class UserReg(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_con_password = models.CharField(max_length=100)