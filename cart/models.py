from django.db import models
from products.models import Product
from django.contrib.auth.models import User
from datetime import datetime
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.

class OrderProduct(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1,validators=[MinValueValidator(1),MaxValueValidator(10)])
    def __str__(self):
        return f"{self.product.name}"


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(OrderProduct)
    total = models.IntegerField()
    created_at = models.DateTimeField(default=datetime.now)
    remove_successful_order = models.BooleanField(default=False )
    def __str__(self):
        return self.user.username
    
