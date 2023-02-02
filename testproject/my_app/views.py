from django.http import JsonResponse
from django.shortcuts import render
from .models import Reg
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.
def landingpage(request):
    if request.method == 'POST':
        name=request.POST['inputName']
        phone = request.POST['inputPhone']
        email = request.POST['email']
        password = request.POST['inputPassword']
        reg=Reg(name=name,phone=phone,email=email,password=password)
        reg.save()

    return render(request, 'index.html')

def listpage(request):
    data=Reg.objects.all()
    p=Paginator(data, 2)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  #
    except PageNotAnInteger:

        page_obj = p.page(1)
    except EmptyPage:

        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request,'lists.html',context)

def check_email(request):
    print('hello')
    email = request.GET.get('email', None)
    print(email)
    data = {
        'is_taken': Reg.objects.filter(email=email).exists()
    }
    return JsonResponse(data)
