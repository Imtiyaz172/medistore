from django.shortcuts import render,redirect
from django.core.paginator import Paginator
from django.db.models import Q,F
from django.http import HttpResponse
from django.http import JsonResponse
from .import models
import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import random, string, os
from django.contrib.auth.decorators import login_required
import hashlib, socket
from .forms import ContactModelForm
from django.db.models import Sum


# Create your views here.
def index(request):
    slider      = models.slider.objects.filter(Status=True).all().order_by("-id")
    service     = models.service.objects.filter(Status=True).order_by("-id")
    top_view    = models.product.objects.filter(Status=True).order_by("view")
    new    = models.product.objects.filter(Status=True).order_by("-id")
    about_us  = models.about_us.objects.filter(Status=True).all()

    context={
        'slider' : slider,
        'service': service,
        'top_view': top_view,
        'new': new,
        'about_us': about_us,

        
    }
    return render(request, "blogapp/index.html",context)

def about_us(request):
    about_us  = models.about_us.objects.filter(Status=True).all()
    context={
        'about_us' : about_us,
    }
    return render(request, "blogapp/about.html",context)


def corona(request):
    about_us  = models.corona.objects.filter(Status=True).all()
    context={
        'about_us' : about_us,
    }
    return render(request, "blogapp/corona.html",context)

def contact(request):
    if request.method=="POST":
        name        = request.POST['name']
        email       = request.POST['email']
        message     = request.POST['message']
        models.user_message.objects.create(name = name, email = email, message = message)
        messages.success(request, "Massage sent to Admin")
    else:
        messages.warning(request, "")
    location  = models.store_location.objects.filter(Status=True).all()

    context={
        'location' : location,
    }
    return render(request, "blogapp/contact.html",context)

def products(request):
    if request.method == "POST":
        search        = request.POST['name']
        blogsearch    = models.product.objects.filter( Status=True, name__icontains = search)
        if blogsearch:
            return render(request, "blogapp/shop.html",{ 'blogsearch' : blogsearch,})
        else:
            messages.warning(request, "No records found.Please try another")
    product     = models.product.objects.filter(Status=True).all()
    paginator = Paginator(product, 6) # Show 6 contacts per page

    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        product = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        product = paginator.page(paginator.num_pages)
    context={
        'product' : product,
    }
    return render(request, "blogapp/shop.html",context)

def beauty(request):
    if request.method == "POST":
        search        = request.POST['tips_name']
        blogsearch    = models.beauty_care.objects.filter( Status=True, tips_name__icontains = search)
        if blogsearch:
            return render(request, "blogapp/beauty.html",{ 'blogsearch' : blogsearch,})
        else:
            messages.warning(request, "No records found.Please try another")
    product     = models.beauty_care.objects.filter(Status=True).all()
    paginator = Paginator(product, 6) # Show 6 contacts per page

    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        product = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        product = paginator.page(paginator.num_pages)
    context={
        'product' : product,
    }
    return render(request, "blogapp/beauty.html",context)




def health(request):
    if request.method == "POST":
        search        = request.POST['name']
        blogsearch    = models.health_care.objects.filter( Status=True, name__icontains = search)
        if blogsearch:
            return render(request, "blogapp/health.html",{ 'blogsearch' : blogsearch,})
        else:
            messages.warning(request, "No records found.Please try another")
    product     = models.health_care.objects.filter(Status=True).all()
    paginator = Paginator(product, 6) # Show 6 contacts per page

    page = request.GET.get('page')
    try:
        product = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        product = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        product = paginator.page(paginator.num_pages)
    context={
        'product' : product,
    }
    return render(request, "blogapp/health.html",context)




def product_detail(request, id):
    product     = models.product.objects.filter(id = id, Status=True).first()
    if request.method=="POST":
        quantity      = request.POST['quantity']
        price      = request.POST['price']
        if request.session.get('id'):
            user_cart = models.Cart.objects.create(
                user_reg_id = int(request.session['id']), product_id = product.id , quantity = quantity,price=price,
            )
            

                    

    
    models.product.objects.filter(id = id).update(view =F('view') + 1)
    context={
        'product' : product,
    }
    return render(request, "blogapp/single.html",context)

def delete_prod(request,id):
        models.Cart.objects.filter(id=id).delete()
        return redirect("/cart")



def tips(request):
    if request.method == "POST":
        search        = request.POST['disease_name']
        blogsearch    = models.tips.objects.filter( Status=True, disease_name__icontains = search)
        if blogsearch:
            return render(request, "blogapp/tips.html",{ 'blogsearch' : blogsearch,})
        else:
            messages.warning(request, "No records found.Please try another")
    tips     = models.tips.objects.filter(Status=True).all()
    paginator = Paginator(tips, 6) # Show 6 contacts per page

    page = request.GET.get('page')
    try:
        tips = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        tips = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        tips = paginator.page(paginator.num_pages)
    context={
        'tips' : tips,
    }
    return render(request, "blogapp/tips.html",context)


def tips_detail(request, id):
    tips_detail     = models.tips.objects.filter(id = id, Status=True).first()
    models.tips.objects.filter(id = id).update(view =F('view') + 1)
    context={
        'tips_detail' : tips_detail,
    }
    return render(request, "blogapp/tipssingle.html",context)


def health_detail(request, id):
    tips_detail     = models.health_care.objects.filter(id = id, Status=True).first()
    models.health_care.objects.filter(id = id).update(view =F('view') + 1)
    context={
        'tips_detail' : tips_detail,
    }
    return render(request, "blogapp/healthdetails.html",context)


def beauty_detail(request, id):
    tips_detail     = models.beauty_care.objects.filter(id = id, Status=True).first()
    models.beauty_care.objects.filter(id = id).update(view =F('view') + 1)
    context={
        'tips_detail' : tips_detail,
    }
    return render(request, "blogapp/beautydetails.html",context)



def cart(request):
    if not request.session['id']:
        return redirect('/login/')
    user_cart      = models.Cart.objects.filter(status = True, user_reg_id = request.session['id']).order_by("-id")
    tatal_amount    = models.Cart.objects.filter(user_reg_id = request.session['id'],status = True).aggregate(total=Sum('price', field="price*quantity") )['total']
    
    print(tatal_amount)
    context={
    'user_cart'    : user_cart,
    
}
    
    return render(request, "blogapp/cart.html",context)



def login(request):
    if request.method=="POST":
        Name     = request.POST['Name']
        password  = request.POST['password']

        new_md5_obj = hashlib.md5(password.encode())
        enc_pass    = new_md5_obj.hexdigest()
        user        = models.user_reg.objects.filter(Name = Name, password = enc_pass)
        if user:
            request.session['email'] = user[0].email
            request.session['id'] = user[0].id
            return redirect("/cart/")
    return render(request, "blogapp/login.html")



def user_register(request):
    if request.method=="POST":
        Name        = request.POST['Name']
        email       = request.POST['email']
        phone       = request.POST['phone']
        password    = request.POST['password']
        new_md5_obj     = hashlib.md5(password.encode())
        new_enc_pass    = new_md5_obj.hexdigest()
        cheak_email = models.user_reg.objects.filter(email = email)

        if not cheak_email:
            models.user_reg.objects.create(Name = Name, email = email, phone = phone, password = new_enc_pass)
            messages.success(request, "Registration Successfull")
            return redirect('/login/')
            
        else:
            messages.warning(request, "Already This Email has an Account")
    else:
        messages.warning(request, "")

    return render(request, "blogapp/reg.html")

def contact(request):
    form = ContactModelForm()
    if request.is_ajax():
        form = ContactModelForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({
                'message': 'success'
            })
    return render(request, 'blogapp/contact.html', {'form': form})



def logout(request):
    request.session['email'] = False
    request.session['id'] = False
    return redirect("/login/")