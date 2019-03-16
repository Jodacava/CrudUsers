from django.db import models

# Create your models here.
class UserClass(models.Model):
    id = models.AutoField(primary_key = True)
    uclassname = models.CharField(max_length = 10)
    description = models.CharField(max_length = 300)

class Users(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    uclass = models.ForeignKey(UserClass, on_delete = models.CASCADE)
    