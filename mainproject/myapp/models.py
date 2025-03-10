from django.db import models

# Create your models here.
class cal(models.Model):
    value_a = models.CharField(max_length=100)
    value_b = models.FloatField(max_length=100)
    result = models.CharField(max_length=100)

    