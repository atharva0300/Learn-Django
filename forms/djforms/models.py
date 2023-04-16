from django.db import models

# Create your models here.
class formModel(models.Model) : 
    name = models.CharField( max_length=50)
    address = models.TextField()
    choice = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    uuid = models.UUIDField()
    floating = models.FloatField()
    number = models.DecimalField(max_digits=5, decimal_places=2)
    checkbox = models.CharField(max_length=50)
    file = models.FileField(upload_to=None, max_length=100)
    email = models.EmailField( max_length=254) 
    cc = models.BooleanField()