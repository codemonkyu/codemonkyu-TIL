from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import customer

def customer_list(request):
    my_name = '장고프레임워크'
    http_method = request.method
    customers = customer.objects.filter(name__contains = 'customer')
    context = { 'customers': customers,}
    return render(request, 'customer/customer_list.html', context)


#글 상세정보
def customer_detail(request, pk):
    customer_key = get_object_or_404(customer, pk=pk)
    return render(request, 'customer/customer_detail.html', {'customer': customer_key})

