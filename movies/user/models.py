from django.db import models

# Create your models here.
class use(models.Model):
    usename = models.CharField(max_length=64)
    def __str__(self):
        return self.usename   
 
class Movie(models.Model):
    movie_id = models.CharField(max_length=16, unique=True, primary_key=True)
    title = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    genres = models.ManyToManyField(use, related_name='movies', db_table='movie_genre')
 
    def __str__(self):
        return self.title
    
class UserPass(models.Model):
    username=models.CharField(max_length=32)
    password=models.CharField(max_length=32)
    