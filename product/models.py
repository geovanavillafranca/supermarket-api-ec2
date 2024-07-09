from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = (
        ('1', 'Fruits and Vegetables'),
        ('2', 'Meat'),
        ('3', 'Beverages'),
        ('4', 'Electronics'),
    )

    name = models.CharField(max_length=70, blank=False, null=False)
    price = models.DecimalField(decimal_places=2, null=False, blank=False, max_digits=7)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    def __str__(self):
        return self.name
    
