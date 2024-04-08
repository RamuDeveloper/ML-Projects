from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
def home(request):
    p1=Products()
    p1.name='Rings'
    p1.price=800
    p1.image='p5.png'
    p1.new=True
    p2=Products()
    p2.name='Bear'
    p2.price=1800
    p2.image='p6.png'
    p2.new=False
    p3=Products()
    p3.name='Flowers'
    p3.price=8000
    p3.image='p4.png'
    p3.new=False
    p4=Products()
    p4.name='Watch'
    p4.price=200
    p4.image='p7.png'
    p4.new=True
    p5=Products()
    p5.name='Watch'
    p5.price=200
    p5.image='p7.png'
    p5.new=True
    p6=Products()
    p6.name='Watch'
    p6.price=200
    p6.image='p7.png'
    p6.new=True
    p6=Products()
    p6.name='Watch'
    p6.price=200
    p6.image='p7.png'
    p6.new=True
    p7=Products()
    p7.name='Watch'
    p7.price=200
    p7.image='p7.png'
    p7.new=True
    
    objs=[p1,p2,p3,p4,p5,p6,p7]
    return render(request,'index.html',{'objs':objs})
# Create your views here.

def add(request):
    return render(request,'form1.html')
def result(request):
   num1=int(request.GET['n1'])
   num2=int(request.GET['n2'])
   res=num1+num2
   return render(request,'results.html',{'result':res})
