from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main import models


@login_required(login_url='dashboard:log_in')
def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()

    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/index.html', context)


# CRUD 

# Create
# Read -> List/Detail
# Update
# Delte

""" Banner section """
@login_required(login_url='dashboard:log_in')
def create_banner(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        models.Banner.objects.create(
            title=title,
            body=body,
        )
    return render(request, 'dashboard/banner/create.html')


@login_required(login_url='dashboard:log_in')
def list_banner(request):
    banners = models.Banner.objects.all()
    context = {
        'banners':banners
    }
    return render(request, 'dashboard/banner/list.html', context)

def detail_banner(request, id):
    banner = models.Banner.objects.get(id=id)
    context = {
        'banner':banner
    }
    return render(request, 'dashboard/banner/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_banner(request, id):
    banner = models.Banner.objects.get(id=id)
    if request.method =='POST':
        banner.title = request.POST['title']
        banner.body = request.POST['body']
        banner.save()
        return redirect('dashboard:banner-detail', banner.id)
    context = {
        'banner':banner
    }
    return render(request, 'dashboard/banner/edit.html', context)

def delete_banner(request, id):
    models.Banner.objects.get(id=id).delete()
    return redirect('banner-list')



""" Service section """
@login_required(login_url='dashboard:log_in')
def create_service(request):
    if request.method == "POST":
        name = request.POST['name']
        body = request.POST['body']
        icon = request.POST['icon']
        models.Service.objects.create(
            name=name,
            body=body,
            icon=icon
        )
    return render(request, 'dashboard/service/create.html')


@login_required(login_url='dashboard:log_in')
def list_service(request):
    services = models.Service.objects.all()
    context = {
        'services':services
    }
    return render(request, 'dashboard/service/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_service(request, id):
    service = models.Service.objects.get(id=id)
    context = {
        'service':service
    }
    return render(request, 'dashboard/service/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_service(request, id):
    service = models.Service.objects.get(id=id)
    if request.method =='POST':
        service.name = request.POST['name']
        service.body = request.POST['body']
        service.icon = request.POST['icon']
        service.save()
        return redirect('dashboard:service-list', service.id)
    context = {
        'service':service
    }
    return render(request, 'dashboard/service/edit.html', context)


@login_required(login_url='dashboard:log_in')
def delete_service(request, id):
    models.Service.objects.get(id=id).delete()
    return redirect('dashboard:service-list')


""" Price section """
@login_required(login_url='dashboard:log_in')
def create_price(request):
    if request.method == "POST":
        title = request.POST['title']
        price = request.POST['price']
        body = request.POST['body']
        models.Price.objects.create(
            title=title,
            price=price,
            body=body
        )
    return render(request, 'dashboard/price/create.html')


@login_required(login_url='dashboard:log_in')
def list_price(request):
    prices = models.Price.objects.all()
    context = {
        'prices':prices
    }
    return render(request, 'dashboard/price/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_price(request, id):
    prices = models.Price.objects.get(id=id)
    context = {
        'prices':prices
    }
    return render(request, 'dashboard/price/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_price(request, id):
    price = models.Price.objects.get(id=id)
    if request.method =='POST':
        price.title = request.POST['title']
        price.price = request.POST['price']
        price.body = request.POST['body']
        price.save()
        return redirect('dashboard:price-list')
    context = {
        'price':price
    }
    return render(request, 'dashboard/price/edit.html', context)


@login_required(login_url='dashboard:log_in')
def delete_price(request, id):
    models.Price.objects.get(id=id).delete()
    return redirect('dashboard:price-list')


""" About us section """
@login_required(login_url='dashboard:log_in')
def create_about_us(request):
    if request.method == "POST":
        body = request.POST['body']
        models.AboutUs.objects.create(
            body=body
        )
    return render(request, 'dashboard/about_us/create.html')


@login_required(login_url='dashboard:log_in')
def list_about_us(request):
    about_us = models.AboutUs.objects.all()
    context = {
        'about_us':about_us
    }
    return render(request, 'dashboard/about_us/list.html', context)

@login_required(login_url='dashboard:log_in')
def detail_about_us(request, id):
    about_us = models.AboutUs.objects.get(id=id)
    context = {
        'about_us':about_us
    }
    return render(request, 'dashboard/about_us/detail.html', context)


@login_required(login_url='dashboard:log_in')
def edit_about_us(request, id):
    about_us = models.AboutUs.objects.get(id=id)
    if request.method =='POST':
        about_us.body = request.POST['body']
        about_us.save()
        return redirect('about_us-list')
    context = {
        'about_us':about_us
    }
    return render(request, 'dashboard/about_us/edit.html', context)

@login_required(login_url='dashboard:log_in')
def delete_about_us(request, id):
    models.AboutUs.objects.get(id=id).delete()
    return redirect('dashboard:about_us-list')


""" Contact section """
@login_required(login_url='dashboard:log_in')
def list_contact(request):   
    contacts = models.Contact.objects.all()
    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/contact/list.html', context)


@login_required(login_url='dashboard:log_in')
def detail_contact(request, id):
    contacts = models.Contact.objects.get(id=id) 
    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/contact/detail.html', context)

@login_required(login_url='dashboard:log_in')
def edit_contact(request, id):
    contact = models.Contact.objects.get(id=id)
    if request.method == "POST":
        is_show = request.POST.get('is_show')  
        contact.is_show = is_show == 'on'
        contact.save()
        return redirect('dashboard:contact-list')
    context = {
        'contact': contact, 
    }
    return render(request, 'dashboard/contact/edit.html', context)


""" Register, login, logout """
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            User.objects.create_user(
                username=username,
                password=password
            )
    return render(request, 'dashboard/auth/register.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard:index')
        else:
            return render(request, 'dashboard/auth/login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'dashboard/auth/login.html')


def log_out(request):
    logout(request)
    return redirect('main:index')