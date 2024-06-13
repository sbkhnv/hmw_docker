from django.db import models
from django.contrib.auth.models import User
from django.db.models import TextChoices


class Category(models.Model):
    name = models.CharField(max_length=20)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'category'


    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    count = models.PositiveIntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.name

class OrderStatus(models.TextChoices):
    PENDING = 'PENDING', 'pending'
    TRANSIT =  'TRANSIT', 'transit'
    DELIVERED = 'DELIVERED', 'delivered'


class Order(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    count = models.PositiveIntegerField(default=1)
    order_status = models.CharField(max_length=10,choices=OrderStatus.choices,default=OrderStatus.PENDING)
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.product.name