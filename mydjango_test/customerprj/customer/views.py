import email
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import customer

def customer_list(request):
    my_name = '장고프레임워크'
    http_method = request.method
    customers = customer.objects.filter(name__contains = 'customer')
    context = { 'customers': customers,}
    return render(request, 'customer/customer_list.html', context)



