from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Customer
from .forms import CustomerFrom


#글 추가(Form)사용
def customer_new(request):
    if request.method == 'POST':
        cus_form = CustomerFrom(request.POST)
        if cus_form.is_valid():
            clean_data_dict = cus_form.cleaned_data
            print(clean_data_dict)
            
            customer = Customer.objects.create(
                name=clean_data_dict['name'],
                email=clean_data_dict['email'],
                birthdate=clean_data_dict['birthdate'],
                gender=clean_data_dict['gender'],
                
            )
            return redirect('customer_detail', pk=customer.pk)        
    else:
        cus_form = CustomerFrom()
    return render(request, 'customer/customer_edit.html', {'form':cus_form})
            


#Views 내에 선언된 함수로 인자로 HttpRequest 라는 객체를 Django가 전달해준다.
def customer_list(request):
    my_name = '장고프레임워크'
    http_method = request.method
    customers = Customer.objects.filter(name__contains = 'customer')
    context = { 'customers': customers,}
    return render(request, 'customer/customer_list.html', context)


#글 상세정보
def customer_detail(request, pk):
    customer_key = get_object_or_404(Customer, pk=pk)
    return render(request, 'customer/customer_detail.html', {'customer': customer_key})

