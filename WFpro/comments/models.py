from django.db import models

# Create your models here.
class com(models.Model):
    email=models.CharField(max_length=100)
    comments=models.TextField()
    def _str_(self):
        return self.title 
