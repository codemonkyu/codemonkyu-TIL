from django.shortcuts import render


from django.http import HttpResponse
def post_list(request):
    return render(request,'blog/post_list.html')

# Create your views here.


#Views 내에 선언된 함수로 인자로 HttpRequest 라는 객체를 Django가 전달해준다.
def post_list(request):
    my_name = '장고프레임워크'
    http_method = request.method
    return HttpResponse('''
        <h2>Welcome {name}</h2>
        <p>Http Method : {method}</p>
        <p>Http headers User-Agent : {header}</p>
        <p>Http Path : {mypath}</p>
    '''.format(name=my_name, method=http_method, header=request.headers['user-agent'], mypath=request.path))