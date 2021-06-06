from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserRegistration
from .models import User

# Create your views here.

def Add_Show(request):
    if request.method == "POST":
        fm = UserRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg= User(name=nm, email=em, password=pw)
            reg.save()
        return HttpResponseRedirect('/')
    else:
        fm = UserRegistration()
    userdata = User.objects.all()
    return render(request, 'crud/addandshow.html', {'form': fm, 'udt': userdata})

# Edit/Update Function

def Update_Data(request, id):
    if request.method =="POST":
        pi = User.objects.get(pk=id)
        fm = UserRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')
    else:
        pi = User.objects.get(pk=id)  
        fm = UserRegistration(instance=pi)
    return render(request, 'crud/updatedetails.html', {'form':fm})

# Delete Function

def Delete_Data(request, id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')
