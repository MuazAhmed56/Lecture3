from django.shortcuts import render
import datetime as date

# Create your views here.
def index(request):
    now=date.datetime.now()
    return render(request,"newyear/index.html",{
        "newyear": now.month==1 and now.day==1})