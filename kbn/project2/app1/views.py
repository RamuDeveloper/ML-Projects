from django.shortcuts import render
from django.http import HttpResponse
from .models import Products
def home(request):
   products=Products.objects.all()
   return render(request,'index.html',{'products':products})
# Create your views here.

def add(request):
    return render(request,'form1.html')
def result(request):
   num1=int(request.GET['n1'])
   num2=int(request.GET['n2'])
   res=num1+num2
   return render(request,'results.html',{'result':res})
