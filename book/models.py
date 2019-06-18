from django.db import models

# Create your models here.
class bookdetils(models.Model):
    title=models.CharField(max_length=32)
    tiems=models.CharField(max_length=50)
    detile=models.TextField()
    imgs=models.CharField(max_length=50)