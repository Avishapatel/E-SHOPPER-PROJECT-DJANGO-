from django.shortcuts import render,HttpResponse
from .models import *
from django.db.models import Count

# Create your views here.
def home(request):
    return HttpResponse("hello")

def index(request):
    c_id=Main_category.objects.annotate(product_count=Count('product'))
    contaxt={'c_id':c_id}
    return render(request,'index.html',contaxt)

def cart(request):
    c_id=Main_category.objects.all()
    contaxt={'c_id':c_id}
    return render(request,'cart.html',contaxt)

def checkout(request):
    c_id=Main_category.objects.all()
    contaxt={'c_id':c_id}
    return render(request,'checkout.html',contaxt)

def contact(request):
    c_id=Main_category.objects.all()
    contaxt={'c_id':c_id}
    return render(request,'contact.html',contaxt)

def detail(request):
    c_id=Main_category.objects.all()
    contaxt={'c_id':c_id}
    return render(request,'detail.html',contaxt)

def shop(request):
    c_id=Main_category.objects.all()
    color_id=Color.objects.all()
    size_id=Size.objects.all()
    sub=request.GET.get('s_id')
    if sub:
        p_id=Product.objects.filter(sub_cat__id=sub)
    else:   
        p_id=Product.objects.all()

    contaxt= {
        "p_id":p_id,
        "c_id":c_id,
        "color_id":color_id,
        "size_id":size_id,
        "sub":sub   
    }
    return render(request,'shop.html',contaxt)

def color_filter(request):
    color=request.GET.get('color')
    print(color)

    if color:
        p_id=Product.objects.filter(color__id=color)
    else:
        p_id=Product.objects.all()
    contaxt={
        "p_id":p_id
    }
    return render(request,'shop.html',contaxt)

def size_filter(request):
    size=request.GET.get('size')
    print(size)
    if size:
        p_id=Product.objects.filter(size__id=size)
    else:
        p_id=Product.objects.all()
    contaxt={
        "p_id":p_id
    }
    return render(request,'shop.html',contaxt)