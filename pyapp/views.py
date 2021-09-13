from django.shortcuts import render,redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from random import random
from django.core.files.storage import FileSystemStorage
# Create your views here.

def TestFun(request):
    return HttpResponse('hello')

def signupfunction(request):
    if request.method=="POST":
        userName=request.POST['Username']
        password=request.POST['pwd']
        reg=Registration.objects.get(username=userName)
        try:
            if userName==reg.username and password==reg.password and reg.user_type==True:
                return redirect ('admin')
            elif userName==reg.username and password==reg.password and reg.user_type==False:
                request.session['logged_user']=reg.id
                return redirect ('student_home')
            else:
                return render (request,'signup.html')
        except reg.DoesNotExist:
            return render (request,'signup.html')        
    return render (request,'signup.html')

def registerfunction(request): 
    if request.method=="POST":
        name=request.POST['Name']
        contact=request.POST['Contact']
        email=request.POST['Email']
        username=request.POST['Username']
        password=request.POST['pwd']
        confirm_password=request.POST['cpwd']
        register=Registration(name=name,contact=contact,email=email,username=username,password=password,confirm_password=confirm_password)
        register.save()
    return render (request,'register.html')

def adminfunction(request):
    return render (request,'admin.html') 

def student_homefunction(request):
    return render (request,'student_home.html')  

def student_detailsfunction(request):
    current_user=request.session['logged_user']
    getdata=Registration.objects.filter(id=current_user)
    return render (request,'student_details.html',{'data': getdata})

def student_updatefunction(request,id):
    if request.method=="POST":
        name=request.POST['Name']
        contact=request.POST['Contact']
        email=request.POST['Email']
        username=request.POST['Username']
        password=request.POST['pwd']
        confirm_password=request.POST['cpwd']
        Registration.objects.filter(id=id).update(name=name,contact=contact,email=email,username=username,password=password,confirm_password=confirm_password)
    return redirect ('student_details') 
     
def editfunction(request,id):
    edit=Registration.objects.get(id=id)
    return render(request,'student_update.html',{'edit_data':edit})

def active_stfunction(request):
    active=Registration.objects.filter(status=True)
    return render (request,'active_st.html',{'act':active})

def inactive_stfunction(request):
    inactive=Registration.objects.filter(status=False)
    return render (request,'inactive_st.html',{'inact':inactive})

def inactivatefunction(request,id):
    Registration.objects.filter(id=id).update(status=False)
    return redirect('active_st')

def activatefunction(request,id):
    Registration.objects.filter(id=id).update(status=True)
    return redirect('inactive_st')




    