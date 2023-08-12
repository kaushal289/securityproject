from django.db import models
from product.models import Product
from customer.models import Customer

class Buyproduct(models.Model):
    buyproduct_id=models.AutoField(auto_created=True,primary_key=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    product_price=models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    product_image = models.CharField(max_length=100)
    product_qty= models.CharField(max_length=100)
    tot_price=models.CharField(max_length=100)
    esewa_id=models.CharField(max_length=128)
    pin=models.CharField(max_length=128)
    location=models.CharField(max_length=100)
    status=models.CharField(max_length=100)
    contact_no=models.CharField(max_length=100)
    class Meta:
        db_table="buyproduct"

