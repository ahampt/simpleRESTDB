from datetime import datetime
from django.db import models

class Data(models.Model):
	Key = models.CharField(max_length=255,unique=True)
	Value = models.TextField(null=True,blank=True)
	CreatedAt= models.DateTimeField(auto_now_add=True)
	UpdatedAt = models.DateTimeField(auto_now=True)
