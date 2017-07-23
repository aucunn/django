from django.db import models


class Regist(models.Model):
    uNo = models.AutoField(primary_key=True)
    uId = models.CharField(max_length=30, unique=True)
    uPass = models.CharField(max_length=30)
    uName = models.CharField(max_length=30)
    uEmail = models.EmailField(max_length=50, unique=True)
    
    def __str__(self):
        return self.uId
# Create your models here.
