from django.db import models

# Create your models here.

class Product(models.Model):
    product_id=models.AutoField(auto_created=True,primary_key=True)
    product_name=models.CharField(max_length=200)
    product_price=models.CharField(max_length=100)
    product_type=models.CharField(max_length=100)
    product_desc=models.CharField(max_length=200)
    product_image=models.FileField(upload_to='product_images')
    class Meta:
        db_table="product"