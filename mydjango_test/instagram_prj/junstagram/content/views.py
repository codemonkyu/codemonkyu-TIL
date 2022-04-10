import email
from django.shortcuts import render
from matplotlib.style import context
from rest_framework.views import APIView
from rest_framework.response import Response
from content.models import Feed
import os
from junstagram.settings import MEDIA_ROOT
from uuid import uuid4
from user.models import User
 
class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id')
        print('로그인한 사용자:', request.session['email'])
        
        email = request.session['email']
        if email is None:
            return render(request, "user/login.html")
        
        
        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, "user/login.html")
        
        return render(request, "junstagram/main.html", context=dict(feeds=feed_list, user=user))



class UploadFeed(APIView):
    def post(self, request):
        
        #파일 불러오기 
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)
        
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        file = request.data.get('file')
        image = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')
        
    
        
        Feed.objects.create(image=image, content=content, user_id=user_id, profile_image=profile_image, like_count=0)
        
       
        return Response(status=200)

class Profile(APIView):
    def get(self, request):
        
        email = request.session['email']
        if email is None:
            return render(request, "user/login.html")
        
        
        user = User.objects.filter(email=email).first()
        if user is None:
            return render(request, "user/login.html")
        
        return render(request, 'content/profile.html', context=dict(user=user))
    
    