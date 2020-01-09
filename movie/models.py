from django.db import models

# Create your models here.
class Movie_action(models.Model):
    num          = models.IntegerField(max_length=1000,verbose_name='电影编号')
    movie_name   = models.CharField(max_length=1000,verbose_name='片名')
    movie_source = models.CharField(max_length=1000,verbose_name='海报路径')
    up_time      = models.CharField(max_length=1000,verbose_name='上映时间')
    movie_adress = models.CharField(max_length=1000,verbose_name='影片归属地')
    director     = models.CharField(max_length=2000,verbose_name='导演')
    actor        = models.CharField(max_length=2000,verbose_name='演员表')
    score        = models.FloatField(max_length=2000,verbose_name='评分')
    story        = models.CharField(max_length=1000, verbose_name='剧情概要')

class Movie_horrible(models.Model):
    num          = models.IntegerField(max_length=1000,verbose_name='电影编号')
    movie_name   = models.CharField(max_length=1000,verbose_name='片名')
    movie_source = models.CharField(max_length=1000,verbose_name='海报路径')
    up_time      = models.CharField(max_length=1000,verbose_name='上映时间')
    movie_adress = models.CharField(max_length=1000,verbose_name='影片归属地')
    director     = models.CharField(max_length=2000,verbose_name='导演')
    actor        = models.CharField(max_length=2000,verbose_name='演员表')
    score        = models.FloatField(max_length=2000,verbose_name='评分')
    story        = models.CharField(max_length=1000, verbose_name='剧情概要')

class Movie_comedy(models.Model):
    num          = models.IntegerField(max_length=1000,verbose_name='电影编号')
    movie_name   = models.CharField(max_length=1000,verbose_name='片名')
    movie_source = models.CharField(max_length=1000,verbose_name='海报路径')
    up_time      = models.CharField(max_length=1000,verbose_name='上映时间')
    movie_adress = models.CharField(max_length=1000,verbose_name='影片归属地')
    director     = models.CharField(max_length=2000,verbose_name='导演')
    actor        = models.CharField(max_length=2000,verbose_name='演员表')
    score        = models.FloatField(max_length=2000,verbose_name='评分')
    story        = models.CharField(max_length=1000, verbose_name='剧情概要')

class Movie_cartoon(models.Model):
    num          = models.IntegerField(max_length=1000,verbose_name='电影编号')
    movie_name   = models.CharField(max_length=1000,verbose_name='片名')
    movie_source = models.CharField(max_length=1000,verbose_name='海报路径')
    up_time      = models.CharField(max_length=1000,verbose_name='上映时间')
    movie_adress = models.CharField(max_length=1000,verbose_name='影片归属地')
    director     = models.CharField(max_length=2000,verbose_name='导演')
    actor        = models.CharField(max_length=2000,verbose_name='演员表')
    score        = models.FloatField(max_length=2000,verbose_name='评分')
    story        = models.CharField(max_length=1000, verbose_name='剧情概要')

class Movie_science(models.Model):
    num          = models.IntegerField(max_length=1000,verbose_name='电影编号')
    movie_name   = models.CharField(max_length=1000,verbose_name='片名')
    movie_source = models.CharField(max_length=1000,verbose_name='海报路径')
    up_time      = models.CharField(max_length=1000,verbose_name='上映时间')
    movie_adress = models.CharField(max_length=1000,verbose_name='影片归属地')
    director     = models.CharField(max_length=2000,verbose_name='导演')
    actor        = models.CharField(max_length=2000,verbose_name='演员表')
    score        = models.FloatField(max_length=2000,verbose_name='评分')
    story        = models.CharField(max_length=1000, verbose_name='剧情概要')

class Movie_crime(models.Model):
    num          = models.IntegerField(max_length=1000,verbose_name='电影编号')
    movie_name   = models.CharField(max_length=1000,verbose_name='片名')
    movie_source = models.CharField(max_length=1000,verbose_name='海报路径')
    up_time      = models.CharField(max_length=1000,verbose_name='上映时间')
    movie_adress = models.CharField(max_length=1000,verbose_name='影片归属地')
    director     = models.CharField(max_length=2000,verbose_name='导演')
    actor        = models.CharField(max_length=2000,verbose_name='演员表')
    score        = models.FloatField(max_length=2000,verbose_name='评分')
    story        = models.CharField(max_length=1000, verbose_name='剧情概要')

class Movie_love(models.Model):
    num          = models.IntegerField(max_length=1000,verbose_name='电影编号')
    movie_name   = models.CharField(max_length=1000,verbose_name='片名')
    movie_source = models.CharField(max_length=1000,verbose_name='海报路径')
    up_time      = models.CharField(max_length=1000,verbose_name='上映时间')
    movie_adress = models.CharField(max_length=1000,verbose_name='影片归属地')
    director     = models.CharField(max_length=2000,verbose_name='导演')
    actor        = models.CharField(max_length=2000,verbose_name='演员表')
    score        = models.FloatField(max_length=2000,verbose_name='评分')
    story        = models.CharField(max_length=1000, verbose_name='剧情概要')

class Movie_story(models.Model):
    num          = models.IntegerField(max_length=1000,verbose_name='电影编号')
    movie_name   = models.CharField(max_length=1000,verbose_name='片名')
    movie_source = models.CharField(max_length=1000,verbose_name='海报路径')
    up_time      = models.CharField(max_length=1000,verbose_name='上映时间')
    movie_adress = models.CharField(max_length=1000,verbose_name='影片归属地')
    director     = models.CharField(max_length=2000,verbose_name='导演')
    actor        = models.CharField(max_length=2000,verbose_name='演员表')
    score        = models.FloatField(max_length=2000,verbose_name='评分')
    story        = models.CharField(max_length=1000, verbose_name='剧情概要')

class Movie_all(models.Model):
    num          = models.IntegerField(max_length=1000,verbose_name='电影编号')
    movie_name   = models.CharField(max_length=1000,verbose_name='片名')
    movie_source = models.CharField(max_length=1000,verbose_name='海报路径')
    up_time      = models.CharField(max_length=1000,verbose_name='上映时间')
    movie_adress = models.CharField(max_length=1000,verbose_name='影片归属地')
    director     = models.CharField(max_length=2000,verbose_name='导演')
    actor        = models.CharField(max_length=2000,verbose_name='演员表')
    score        = models.FloatField(max_length=2000,verbose_name='评分')
    story        = models.CharField(max_length=1000, verbose_name='剧情概要')
