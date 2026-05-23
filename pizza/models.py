from django.db import models



class size(models.TextChoices):
    SMALL = 'S', 'Small'
    MEDIUM = 'M', 'Medium'
    LARGE = 'L', 'Large'

TOPPING_CHOICES = [
    ('pepperoni', 'Pepperoni'),
    ('mushrooms', 'Mushrooms'),
    ('onions', 'Onions'),
]

# Create your models here.
class Pizza(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    size = models.CharField(max_length=1, choices=size.choices, default=size.MEDIUM)
    toppings = models.JSONField(default=list, blank=True, null=True)
    image = models.ImageField(upload_to='pizza_images/', blank=True, null=True)


    def __str__(self):
        return self.name
