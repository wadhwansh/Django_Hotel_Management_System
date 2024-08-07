from django.db import models

# Create your models here.
class feedback(models.Model):
    Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Phone=models.IntegerField()
    Review=models.TextField()