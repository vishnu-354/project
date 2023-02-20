from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from django.utils.datastructures import MultiValueDictKeyError

from app1.models import admindb, categorydb, productdb
from frontend.models import contactdb


# Create your views here.
def index(req):
    return render(req, "index.html")

def adminpage(req):
    return render(req, "addadmin.html")

def admin(req):
    if req.method == "POST":
        na = req.POST.get('Name')
        em = req.POST.get('Email')
        mo = req.POST.get('Mobileno')
        us = req.POST.get('Username')
        pa = req.POST.get('Password')
        img = req.FILES['image']
        obj = admindb(Name=na,  Email=em, Mobileno=mo, Username=us, Password=pa, image=img)
        obj.save()
        return redirect(adminpage)


def displayadmin(req):
    data = admindb.objects.all()
    return render(req, 'displayadmin.html', {'data': data})

def editadmin(req, dataid):
    data = admindb.objects.get(id=dataid)
    print(data)
    return render(req, "editadmin.html", {'data': data})

def updateadmin(req, dataid):
    if req.method == "POST":
        na = req.POST.get('Name')
        em = req.POST.get('Email')
        mo = req.POST.get('Mobileno')
        us = req.POST.get('Username')
        pa = req.POST.get('Password')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = admindb.objects.get(id=dataid).image
        admindb.objects.filter(id=dataid).update(Name=na,  Email=em, Mobileno=mo, Username=us, Password=pa,  image=file)
        return redirect(displayadmin)

def deleteadmin(req, dataid):
    data = admindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)


def addcategory(req):
    return render(req, "addcategory.html")


def category(req):
    if req.method == "POST":
        na = req.POST.get('Name')
        de = req.POST.get('Description')
        img = req.FILES['image']
        obj = categorydb(Name=na, Description=de, image=img)
        obj.save()
        return redirect(addcategory)

def displaycategory(req):
    data = categorydb.objects.all()
    return render(req, 'displaycategory.html', {'data': data})

def editcategory(req, dataid):
    data = categorydb.objects.get(id=dataid)
    print(data)
    return render(req, "editcategory.html", {'data': data})

def updatecategory(req, dataid):
    if req.method == "POST":
        na = req.POST.get('Name')
        de = req.POST.get('Description')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).image
        categorydb.objects.filter(id=dataid).update(Name=na,  Description=de,  image=file)
        return redirect(displaycategory)

def deletecategory(req, dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategory)

def addproduct(req):
    data = categorydb.objects.all()
    return render(req, "addproduct.html", {'data':data})

def product(req):
    if req.method == "POST":
        ca = req.POST.get('Category')
        pn = req.POST.get('Productname')
        pr = req.POST.get('Price')
        qu = req.POST.get('Quantity')
        de = req.POST.get('Description')
        img = req.FILES['image']
        obj = productdb(Category=ca,Productname=pn, Price=pr,Quantity=qu, Description=de, image=img)
        obj.save()
        return redirect(addproduct)

def displayproduct(req):
    data = productdb.objects.all()
    return render(req, 'displayproduct.html', {'data': data})

def editproduct(req, dataid):
    data = productdb.objects.get(id=dataid)
    da = categorydb.objects.all()
    print(data)
    return render(req, "editproduct.html", {'data': data, 'da': da})

def updateproduct(req, dataid):
    if req.method == "POST":
        ca = req.POST.get('Category')
        pn = req.POST.get('Productname')
        pr = req.POST.get('Price')
        qu = req.POST.get('Quantity')
        de = req.POST.get('Description')
        try:
            img = req.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=dataid).image
        productdb.objects.filter(id=dataid).update(Category=ca,Productname=pn, Price=pr,Quantity=qu, Description=de, image=file)
        return redirect(displayproduct)

def deleteproduct(req, dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproduct)




def logina(req):
    return render(req, "login.html")

def adminlogin(req):
    if req.method=="POST":
        username_r = req.POST.get('username')
        password_r = req.POST.get('password')
        if User.objects.filter(username__contains= username_r).exists():
            user= authenticate(username= username_r,password = password_r)
            if user is not None:
                login(req, user)
                req.session['username']= username_r
                req.session['password']= password_r
                return redirect(index)
            else:
                return redirect(logina)
        else:
            return redirect(logina)

def adminlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(logina)

def customers(req):
    data = contactdb.objects.all()
    return render(req, 'customers.html',{'data':data})

def deletecustomer(req, dataid):
    data = contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(customers)