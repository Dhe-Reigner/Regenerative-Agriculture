from django.db import models

# Create your models here.
class RegisterUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class LoginUser(models.Model):
    user = models.OneToOneField(RegisterUser, on_delete=models.CASCADE)
    password = models.CharField(max_length=100)
    
    