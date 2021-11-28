from django.db import models
from django.urls import reverse

# Create your models here.

class AllProduct(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=200,decimal_places=2)
    description = models.TextField(default="")

    def __str__(self):
        return self.title

class iPhoneModel(models.Model):
    title = models.CharField(max_length=400)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length = 400)
    image = models.ImageField(upload_to="images/product_imgs")
    detail = models.TextField(default='')
    price = models.DecimalField(decimal_places=2,max_digits=10000)
    model = models.ForeignKey(iPhoneModel,on_delete=models.CASCADE)
    slug = models.SlugField()
    

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})

        
