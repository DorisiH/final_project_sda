from django.db import models
from users.models import CustomUser
from menu.models import Product


class Cart(models.Model):
    customer_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class Order(models.Model):
    order_date = models.DateTimeField()
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=6, decimal_places=2)


class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    item_quantity = models.IntegerField()
    product_name = models.CharField(max_length=25)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)



