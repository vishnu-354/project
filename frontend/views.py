from django.shortcuts import render, redirect

from app1.models import categorydb, productdb
from frontend.models import customerdb, contactdb, deliveries

from django.contrib import messages


# Create your views here.
def homei(req):
    data = categorydb.objects.all()
    return render(req, "home.html",{'data':data})



def discategory(req,itemcatg):
    data = categorydb.objects.all()
    print("=====itemcatg======",itemcatg)
    catg=itemcatg.upper()

    products=productdb.objects.filter(Category= itemcatg)
    context={
        'products' : products,
        'catg' : catg,
        'data' : data
    }
    return render(req,"categories.html", context)


def prosingle(req, dataid):
    da = categorydb.objects.all()
    data= productdb.objects.get(id=dataid)
    return render(req, "productsingle.html", {'data': data, 'da':da})

def  login1(req):
    return render(req, "loginuser.html")

def customer(req):
    if req.method == "POST":
        us = req.POST.get('Username')
        em = req.POST.get('Email')
        pa = req.POST.get('Password')
        co = req.POST.get('Confirmpassword')
        if pa == co:
            obj = customerdb(Username=us, Email=em, Password=pa, Confirmpassword=co)
            obj.save()
            # messages.success(req, "register successfully")
            return redirect(login1)
        else:
            # messages.error(req, "redister error")
            return render(req, "loginuser.html", {'msg': "sorryyyyyyyy"} )

def customerlogin(request):
    if request.method == "POST":
        username_r=request.POST.get("username")
        password_r=request.POST.get("password")
        if customerdb.objects.filter(Username=username_r,Password=password_r).exists():
            request.session['username']= username_r
            request.session['password']= password_r
            # messages.error(request, "DONT [PLAY]")
            return redirect(homei)
        else:
            messages.error(request, "DONT [PLAY]")
            return render(request, "loginuser.html", {'msg': "sorryyyyyyyy"})
def contact1(req):
    return render(req, "contact1.html")

def contacte(req):
    if req.method == "POST":
        na = req.POST.get('Name')
        em = req.POST.get('Email')
        su = req.POST.get('Subject')
        me = req.POST.get('Message')
        obj = contactdb(Name=na, Email=em, Subject=su, Message=me)
        obj.save()
        return redirect(contact1)

def adminlogout(req):
    del req.session['username']
    del req.session['password']
    return redirect(login1)


def check(req):
    return render(req, "checkout.html")

def boo(req):
    if req.method=="POST":
        na = req.POST.get('name')
        ad = req.POST.get('address')
        em = req.POST.get('email')
        qt = req.POST.get('qty')
        to = req.POST.get('totalprice')
        obj=deliveries(name=na,address=ad,email=em, qty=qt, totalprice=to)
        obj.save()
        return redirect(homei)