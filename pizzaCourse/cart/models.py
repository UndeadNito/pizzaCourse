from django.db import models
from django.contrib.contenttypes.models import ContentType

from mainapp.models import PizzaModel as Product


class Cart(models.Model):
    creation_date = models.DateTimeField(verbose_name='creation date')
    checked_out = models.BooleanField(default=False, verbose_name='checked out')

    class Meta:
        verbose_name = 'cart'
        verbose_name_plural = 'carts'
        ordering = ('-creation_date',)


class ItemManager(models.Manager):
    def get(self, *args, **kwargs):
        if 'product' in kwargs:
            kwargs['object_id'] = kwargs['product'].pk
            del(kwargs['product'])
        return super(ItemManager, self).get(*args, **kwargs)

    def filter(self, *args, **kwargs):
        if 'product' in kwargs:
            kwargs['object_id'] = kwargs['product'].pk
            del(kwargs['product'])
        return super(ItemManager, self).filter(*args, **kwargs)


class Item(models.Model):
    cart = models.ForeignKey(Cart, verbose_name='cart', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='quantity')
    object = models.ForeignKey(Product, on_delete=models.CASCADE)

    objects = ItemManager()

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'
        ordering = ('cart',)

    def __unicode__(self):
        return u'%d units of %s' % (self.quantity, self.product.__class__.__name__)

    def total_price(self):
        return self.quantity * self.unit_price
    total_price = property(total_price)

    # product
    def get_product(self):
        return self.content_type.get_object_for_this_type(pk=self.object_id)

    def set_product(self, product):
        self.content_type = ContentType.objects.get_for_model(type(product))
        self.object_id = product.pk

    product = property(get_product, set_product)


class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_number = models.PositiveIntegerField()
    customer_address = models.TextField(max_length=1024)


class OrderList(models.Model):
    order_id = models.PositiveIntegerField()
    customer = models.ForeignKey(Customer, verbose_name='Customer', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    done = models.BooleanField(default=False)
