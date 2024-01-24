from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=254)
    icon = models.CharField(max_length=254)
    description = models.TextField()

    def __str__(self) -> str:
        return str(self.name)
    
class Information(models.Model):
    name = models.CharField(max_length=254)
    phone = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    location = models.CharField(max_length=254)

    def __str__(self) -> str:
        return str(self.name)
    
class Contact(models.Model):
    name = models.CharField(max_length=254)
    email = models.CharField(max_length=254)
    subject = models.CharField(max_length=254)
    message = models.TextField()

    def __str__(self) -> str:
        return str(self.name)
