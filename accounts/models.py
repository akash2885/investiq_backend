from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    password=models.CharField(max_length=225)
    username=models.CharField(max_length=225,unique=True)
    last_login=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    access_token=models.CharField(max_length=725,null=True,blank=True)

    def get_role_name(self):
        return self.role.name if self.role.name else None
