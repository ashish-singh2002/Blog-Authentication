from django.db import models

class Ashish(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    timestamp = models.DateTimeField() 
    

