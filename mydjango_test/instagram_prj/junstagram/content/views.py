from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed



class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')
        
        #이게 몰 뜻함? select * from content_feed;
        

        return render(request, "junstagram/main.html", context=dict(feeds=feed_list))








