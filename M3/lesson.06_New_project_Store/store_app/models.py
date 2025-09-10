from django.db import models

# Create your models here.
class Catolog(models.Model):
    """каталог продуктов"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    """продукты"""
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    catolog = models.ForeignKey(Catolog, on_delete=models.CASCADE)

    def __str__(self):
        return self.name