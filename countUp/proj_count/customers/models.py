from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=80)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.name)