from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=25, null=False)


class Product(models.Model):
    product_name = models.CharField(max_length=30, null=False)
    product_description = models.TextField(max_length=300)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(null=True)




