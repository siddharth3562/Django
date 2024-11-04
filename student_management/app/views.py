from django.shortcuts import render,redirect

std=[]

def home(req):
    if req.method=='POST':
        roll=req.POST['roll_no']
        name=req.POST['name']
        age=req.POST['age']
        std.append({'roll_no':roll,'name':name,'age':age})
        return redirect(home)
    else:
        return render(req,'home.html',{'students':std})
