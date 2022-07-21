
from django.db import models


class Customer(models.Model):
    CATEGORY_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    birthdate = models.DateField()
    gender = models.CharField(max_length=200, choices=CATEGORY_CHOICES)
    text = models.TextField(default = "특이사항: ")
    
    
    
    def __str__(self):
        return self.name + '(' + str(self.id) + ')'
    
