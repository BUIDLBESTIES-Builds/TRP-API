
from django.db import models
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
# Create your models here.

Category_Choices =(
    ("pre-payed", "pre-payed"),
    ("miscellaneous", "miscellaneous")
)

reimburse_status = (
    ("PENDING", "PENDING"),
    ("APPR0VED", "APPR0VED")
)

Crypto_Choices = (
    ("ETH", "ETH"),
    ("USDT", "USDT")
    
)

class User(models.Model):
   fullname = models.CharField(max_length=100, blank=True)
   category = models.CharField(choices=Category_Choices, max_length=100, blank=True)
   description = models.CharField(max_length=100, blank=True)
   amounts = models.DecimalField(max_digits=6, decimal_places=2, blank=True)
   status = models.CharField(choices=reimburse_status, max_length=20, blank=True)

class Reimbursement(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    wallets = models.CharField(max_length=10000, blank=True)
    crypto = models.CharField(choices=Crypto_Choices, max_length=100, blank=True)
    upload = models.FileField(upload_to='uploads/', blank=True)
    status = models.CharField(choices=reimburse_status, max_length=20, blank=True)


