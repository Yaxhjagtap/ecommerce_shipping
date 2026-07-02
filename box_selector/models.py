from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    # Dimensions can be stored in cm/inches (ensure you enforce a standard unit across your app)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    height = models.DecimalField(max_digits=10, decimal_places=2)
    # Weight can be stored in kg/lbs
    weight = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} ({self.length}x{self.width}x{self.height}, {self.weight})"


class Box(models.Model):
    name = models.CharField(max_length=255)
    internal_length = models.DecimalField(max_digits=10, decimal_places=2)
    internal_width = models.DecimalField(max_digits=10, decimal_places=2)
    internal_height = models.DecimalField(max_digits=10, decimal_places=2)
    max_weight_capacity = models.DecimalField(max_digits=10, decimal_places=2)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.name} (Max Wt: {self.max_weight_capacity} | Cost: ${self.cost})"