# Generated by Django 3.2.9 on 2021-11-28 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_allproduct_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='iPhoneModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='images/product_imgs')),
                ('slug', models.CharField(max_length=400)),
                ('detail', models.TextField(default='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.iphonemodel')),
            ],
        ),
    ]
