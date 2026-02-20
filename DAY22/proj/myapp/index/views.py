from django.shortcuts import render,HttpResponse


def index(request):
    return render(request,'index.html')
# Create your views here.
def home(request):
    return HttpResponse("this is the home page")
def login(request):
    return render(request,"login.html")
def product(request):
    return render(request,"product.html")
def register(request):
    return render(request,"register.html")
def productdata(request):
    return HttpResponse(request,"productdata.html")