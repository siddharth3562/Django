from django.shortcuts import render,redirect
from .models import *
std=[]

def home(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        # std.append({'roll_no':roll,'name':name,'age':age})
        data=Student.objects.create(roll_no=roll,name=name,age=age)
        data.save()
        return redirect(home)
    else:
        data=Student.objects.all()
        return render(req,'home.html',{'students':data})

def edit_std(req,id):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        Student.objects.filter(pk=id).update(roll_no=roll,name=name,age=age)
        return redirect(home)
    else:
        data=Student.objects.get(pk=id)
        return render(req,'edit.html',{'data':data})
    
def delete(req,id):
    data=Student.objects.get(pk=id)
    data.delete()
    return redirect(home)