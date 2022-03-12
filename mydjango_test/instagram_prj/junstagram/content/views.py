from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed



class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all() #이게 몰 뜻함? select * from content_feed;
        
        
        context={'feed_list':feed_list}
        return render(request, "junstagram/main.html", context)








