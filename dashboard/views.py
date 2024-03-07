from django.shortcuts import render, redirect
from main import models

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

def create_banner(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        models.Banner.objects.create(
            title=title,
            body=body,
        )
    return render(request, 'dashboard/banner/create.html')


def list_banner(request):
    banners = models.Banner.objects.all()
    context = {
        'banners':banners
    }
    return render(request, 'dashboard/banner/list.html', context)


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


def list_service(request):
    services = models.Service.objects.all()
    context = {
        'services':services
    }
    return render(request, 'dashboard/service/list.html', context)


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


def list_price(request):
    price = models.Price.objects.all()
    context = {
        'price':price
    }
    return render(request, 'dashboard/price/list.html', context)


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


def list_price(request):
    price = models.Price.objects.all()

    prices_list = []

    for price in models.Price.objects.all().order_by('price'):
        price.body = price.body.split(',')
        prices_list.append(price)

    context = {
        'prices':prices_list
    }
    return render(request, 'dashboard/price/list.html', context)


def create_about_us(request):
    if request.method == "POST":
        body = request.POST['body']
        models.AboutUs.objects.create(
            body=body
        )
    return render(request, 'dashboard/about_us/create.html')


def list_about_us(request):
    about_us = models.AboutUs.objects.all()
    context = {
        'about_us':about_us
    }
    return render(request, 'dashboard/about_us/list.html', context)

def create_contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        body = request.POST['body']
        models.Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            body=body
        )
    return render(request, 'dashboard/contact/create.html')


def list_contact(request):   
    contact = models.Contact.objects.all()
    context = {
        'contact':contact
    }
    return render(request, 'dashboard/contact/list.html', context)
