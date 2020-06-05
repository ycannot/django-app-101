from django.db import models

# Create your models here.

class AppUser(models.Model):
    username = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "Username: " + self.username

class SigninResponse(models.Model):
    status = models.BooleanField
    message = models.CharField(max_length=50)
    token = models.CharField(max_length=100)
    response_created = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=20)
    
    
    def __str__(self):
        
        if status == True:
            return username
        else:
            return "Failed"
        