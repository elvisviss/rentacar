from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.brand} {self.model}"