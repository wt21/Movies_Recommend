from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=16,unique=True)
    age = models.IntegerField(default = 18,db_column='age')
    #False:男   True:女
    sex = models.BooleanField(default = False,db_column='sex')
    class Meta:
        db_table = 'Person'

class User(models.Model):
    username = models.CharField(max_length=16,unique=True)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    state = models.IntegerField(blank=True,null=True)
    class Meta:
        db_table = 'User'