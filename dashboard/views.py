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

""" Banner section """
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

def detail_banner(request, id):
    banner = models.Banner.objects.get(id=id)
    context = {
        'banner':banner
    }
    return render(request, 'dashboard/banner/detail.html', context)


def edit_banner(request, id):
    banner = models.Banner.objects.get(id=id)
    if request.method =='POST':
        banner.title = request.POST['title']
        banner.body = request.POST['body']
        banner.save()
        return redirect('banner-detail', banner.id)
    context = {
        'banner':banner
    }
    return render(request, 'dashboard/banner/edit.html', context)

def delete_banner(request, id):
    models.Banner.objects.get(id=id).delete()
    return redirect('banner-list')



""" Service section """
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

def detail_service(request, id):
    service = models.Service.objects.get(id=id)
    context = {
        'service':service
    }
    return render(request, 'dashboard/service/detail.html', context)


def edit_service(request, id):
    service = models.Service.objects.get(id=id)
    if request.method =='POST':
        service.name = request.POST['name']
        service.body = request.POST['body']
        service.icon = request.POST['icon']
        service.save()
        return redirect('list-service', service.id)
    context = {
        'service':service
    }
    return render(request, 'dashboard/service/edit.html', context)

def delete_service(request, id):
    models.Service.objects.get(id=id).delete()
    return redirect('list-service')


""" Price section """
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
    prices = models.Price.objects.all()
    context = {
        'prices':prices
    }
    return render(request, 'dashboard/price/list.html', context)


def detail_price(request, id):
    pricess = models.Price.objects.get(id=id)
    context = {
        'pricess':pricess
    }
    return render(request, 'dashboard/price/detail.html', context)


def edit_price(request, id):
    prices = models.Price.objects.get(id=id)
    if request.method =='POST':
        prices.title = request.POST['title']
        prices.price = request.POST['price']
        prices.body = request.POST['body']
        prices.save()
        return redirect('price-list')
    context = {
        'prices':prices
    }
    return render(request, 'dashboard/price/edit.html', context)

def delete_price(request, id):
    models.Price.objects.get(id=id).delete()
    return redirect('price-list')


""" About us section """
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

def detail_about_us(request, id):
    about_us = models.AboutUs.objects.get(id=id)
    context = {
        'about_us':about_us
    }
    return render(request, 'dashboard/about_us/detail.html', context)


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

def delete_about_us(request, id):
    models.AboutUs.objects.get(id=id).delete()
    return redirect('about_us-list')


""" Contact section """

def list_contact(request):   
    contacts = models.Contact.objects.all()
    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/contact/list.html', context)

def detail_contact(request, id):
    contacts = models.Contact.objects.get(id=id) 
    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/contact/detail.html', context)

def edit_contact(request, id):
    contacts = models.Contact.objects.get(id=id)
    if request.method == "POST":
        contacts.is_show = request.POST['is_show']
        contacts.save()
        return redirect('contact-list',contacts.id)
    context = {
        'contacts':contacts,
    }
    return render(request, 'dashboard/contact/edit.html', context)


