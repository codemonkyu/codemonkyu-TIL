from django.db import models
from django.urls import reverse
# Create your models here.




#글의 분류 
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="글의 분류를 입력하세요...")
    
    def __str__(self):
        return self.name
    


#블로그 글
class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    def __str___(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("single", args=[str(self.id)])
    
    
