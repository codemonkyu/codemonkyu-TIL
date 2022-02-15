from django.contrib import admin


# Register your models here. #내가만든 model을 추가해줘서 웹브라우져에서 확인하게해주자.
from .models import Movie

admin.site.register(Movie)