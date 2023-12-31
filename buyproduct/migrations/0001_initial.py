# Generated by Django 4.0 on 2022-02-06 03:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyproduct',
            fields=[
                ('buyproduct_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.CharField(max_length=100)),
                ('product_type', models.CharField(max_length=100)),
                ('product_image', models.CharField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'db_table': 'buyproduct',
            },
        ),
    ]
