from django.db import models

# Create your models here.
class Product(models.Model):

    product_id = models.IntegerField()
    product_name = models.TextField()
    product_price = models.FloatField()
    product_quantity = models.IntegerField()

    # def __str__(self):
    #     return self.product_name

    def publish(self):
        self.save()