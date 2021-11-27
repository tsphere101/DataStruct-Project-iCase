from django.db import models

# Create your models here.

class AllProduct(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=200,decimal_places=2)
    description = models.TextField(default="")

    def __str__(self):
        return self.title

        
