from django.db import models

# Create your models here.
class newsletter(models.Model):
    def __str__(self):
        return self.email
    email=models.EmailField(max_length=200)


class contact(models.Model):
    def __str__(self):
        return self.name 
    
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=200)
    msg=models.TextField()
    