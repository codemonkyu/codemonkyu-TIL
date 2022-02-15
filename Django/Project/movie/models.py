from distutils.command.upload import upload
from sre_constants import CATEGORY
from django.db import models


# Create your models here.

#지원하는 모델필드 정리하기

#category같은 경우 여러개중 하나를 선택가능하게 해준다.

CATEGORY_CHOICES = (
    ('A','ACTION'),
    ('B','DRAMA'),
    ('C','COMEDY'),
    ('D','ROMANCE'),
)

LANGUAGE_CHOICES = (
    ('EN','ENGLISH'),
    ('KO','KOREAN'),
)


STATUS_CHOICES = (
    ('RA', 'RECENTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED'),
)



class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=1)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=2)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
        




#tags
# dowload links
# watch links