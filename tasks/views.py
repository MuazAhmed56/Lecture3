from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
tasks=[] # tasks start as an empty list
class NewTaskForm(forms.Form):
    task=forms.CharField(label="New Task")
    priority=forms.IntegerField(label="Set Priority",min_value=1,max_value=5)
# Create your views here.
def index(request):
    return render(request,"tasks/index.html",{
        "tasks":tasks
        })
def add(request):
    if request.method =="POST":
        form=NewTaskForm(request.POST)  # populating the form
        if form.is_valid():   #server side validation
            task=form.cleaned_data["task"]  # attaining the value 
                                            # of our interest which is of task
            tasks.append(task)  # user entered task is added to the list
            return HttpResponseRedirect(reverse("tasks:index"))
            # telling django to reverse engineer the url with name index
            # and redirect you there
        else:
            return render(request,"tasks/add.html",{"form":form}) 
        #the populated form object to the class NewTaskForm is passed 
        #as the Django template variable which will affect the add.html file 
            
    return render(request,"tasks/add.html",{"form":NewTaskForm()})
    #the unpopulated class NewTaskForm is passed 
    #as the Django template variable which will affect the add.html file 