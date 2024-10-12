from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Msg
# Create your views here.
def create(request):
    print("my current request is",request.method)
    if request.method == "POST":
        nm=request.POST["uname"]
        print(nm)
        em=request.POST["uemail"]
        print(em)
        mob=request.POST["umobile"]
        print(mob)
        msg=request.POST["msg"]
        print(msg)
        m=Msg.objects.create(name=nm,email=em,mobile=mob,message=msg)
        m.save()
        return redirect("/dashboard")
    else:
        return render(request,"create.html")

def dashboard(request):
    m=Msg.objects.all()
    
    context={}
    context["data"]=m

    return render(request,'dashboard.html',context)

def delete(request,rid):
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')

def edit(request,rid):
    if request.method=="GET":
        m=Msg.objects.filter(id=rid)
        context={}
        context["data"]=m
        return render(request,'edit.html',context)
    else:
        nm=request.POST["uname"]
        em=request.POST["uemail"]
        mob=request.POST["umobile"]
        msg=request.POST["msg"]
        m=Msg.objects.filter(id=rid)
        m.update(name=nm,email=em,mobile=mob,message=msg)
        return redirect('/dashboard')