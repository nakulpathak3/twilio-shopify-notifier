from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from shopify_auth.models import AbstractShopUser
# Create your models here.

class ShopifyAppShopUser(AbstractShopUser):
    pass

class ProductPreferencesModel(models.Model):
    min_quantity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)], blank=True, default=10)
    text = models.BooleanField(default=False)
    call = models.BooleanField(default=False)
