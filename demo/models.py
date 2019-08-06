from django.db import models
from django.contrib import admin
# Create your models here.

class Post(models.Model):
    title =models.CharField(max_length=100)
    body=models.TextField();
    timeStamp=models.DateTimeField();
    autoor=models.CharField(max_length=30)

admin.site.register(Post) 