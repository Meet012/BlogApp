from django.db import models
from datetime import datetime

# Create your models here.
class blogs(models.Model):
    title = models.CharField(max_length=50)
    dec = models.CharField(max_length=100000000000000)
    created_at = models.DateTimeField(default=datetime.now,blank=True)