from django.db import models


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)  # max_length = required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField()

    # new feature added after DB was created.
    featured = models.BooleanField()  # options: null=True -> All previous items can be empty, default=True
    # default value can be set also after migration
