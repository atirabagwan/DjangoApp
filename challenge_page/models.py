from django.db import models
from datetime import datetime 

# Create your models here.

class challenge(models.Model):
	title = models.CharField(max_length=100)
	deadline = models.DateField(default=datetime.now)
	tags = models.CharField(max_length=100)