from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=11, decimal_places=2)

    """
            This method is used to display the product's
             name and price in the Django admin interface or when the object is printed.
    """
    def __str__(self):
        return f'{self.name}, {self.price}'
