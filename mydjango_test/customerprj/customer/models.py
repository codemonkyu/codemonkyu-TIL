from django.utils import timezone
from django.db import models


class Customer(models.Model):
    
    CATEGORY_CHOICES = {
        ('man','Male'),
        ('woman','Female'),
        ('gay','gay'),
        ('transgender','transgender'),
    }
    # choice (저장값,디스플레이)
    
    name = models.CharField(max_length = 20, default= 'customer_')
    birthdate = models.DateField()
    text = models.TextField(max_length = 100, default=("customer info:"))
    email = models.EmailField(max_length = 50, default=("@"))
    gender = models.CharField(max_length = 40, choices=CATEGORY_CHOICES)
    Join_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name + '(' + str(self.id) + ')'
    
