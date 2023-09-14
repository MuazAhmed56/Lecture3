from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("Hello succkers!")
    return render(request,"hello/index.html")
def brian(request):
    return HttpResponse("Hello Brian modafoka")
def david(request):
    return HttpResponse("hello David Dickless")
def greet(request, name):
    return render(request,"hello/greet.html",{
        "name":name.capitalize()})