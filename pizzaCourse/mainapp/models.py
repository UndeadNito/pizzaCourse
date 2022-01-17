from django.db import models


class PizzaModel(models.Model):

    title = models.CharField(max_length=255, verbose_name='Pizza title')
    description = models.TextField(max_length=1023, verbose_name='Pizza description')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Pizza price')
    image = models.ImageField()

    def __STR__(self):
        return self.title
