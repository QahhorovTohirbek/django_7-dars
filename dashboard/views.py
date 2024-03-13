from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from main import models
from django.contrib import messages



@login_required(login_url='dashboard:log_in')
def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()
    users = User.objects.count()
    services = models.Service.objects.all().count()

    context = {
        'contacts':contacts,
        'users':users,
        'services':services,
    }
    return render(request, 'dashboard/index.html', context)

@login_required(login_url="dashboard:log_in")
def users_list(request):
    users = User.objects.all()
    context = {
        'users':users,
    }
    return render(request, 'dashboard/users_list.html', context)

@login_required(login_url='dashboard:log_in')
def create_banner(request):
    """ Banner section """
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        models.Banner.objects.create(
            title=title,
            body=body,
        )
        messages.success(request, 'Banner muvoffaqiyatli yaratildi')
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
        messages.success(request, 'Banner muvoffaqiyatli yangilandi')
        return redirect('dashboard:banner-detail', banner.id)
    context = {
        'banner':banner
    }
    return render(request, 'dashboard/banner/edit.html', context)

def delete_banner(request, id):
    models.Banner.objects.get(id=id).delete()
    messages.success(request, 'Banner muvoffaqiyatli o`chirildi')
    return redirect('dashboard:banner-list')



@login_required(login_url='dashboard:log_in')
def create_service(request):
    """ Service section """
    if request.method == "POST":
        name = request.POST['name']
        body = request.POST['body']
        icon = request.POST['icon']
        models.Service.objects.create(
            name=name,
            body=body,
            icon=icon
        )
        messages.success(request, 'Service muvoffaqiyatli qo`shildi')
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
        messages.success(request, 'Service muvoffaqiyatli tahrirlandi')
        return redirect('dashboard:service-list')
    context = {
        'service':service
    }
    return render(request, 'dashboard/service/edit.html', context)


@login_required(login_url='dashboard:log_in')
def delete_service(request, id):
    models.Service.objects.get(id=id).delete()
    messages.success(request, 'Service muvoffaqiyatli o`chirildi')
    return redirect('dashboard:service-list')


@login_required(login_url='dashboard:log_in')
def create_price(request):
    """ Price section """
    if request.method == "POST":
        title = request.POST['title']
        price = request.POST['price']
        body = request.POST['body']
        models.Price.objects.create(
            title=title,
            price=price,
            body=body
        )
        messages.success(request, 'Price muvoffaqiyatli qo`shildi')
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
        messages.success(request, 'Price muvoffaqiyatli tahrirlandi')
        return redirect('dashboard:price-list')
    context = {
        'price':price
    }
    return render(request, 'dashboard/price/edit.html', context)


@login_required(login_url='dashboard:log_in')
def delete_price(request, id):
    models.Price.objects.get(id=id).delete()
    messages.success(request, 'Price muvoffaqiyatli o`chirildi')
    return redirect('dashboard:price-list')


@login_required(login_url='dashboard:log_in')
def create_about_us(request):
    """ About us section """
    if request.method == "POST":
        body = request.POST['body']
        models.AboutUs.objects.create(
            body=body
        )
        messages.success(request, 'About us muvoffaqiyatli yaratildi')
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
        messages.success(request, 'About us muvoffaqiyatli tahrirlandi')
        return redirect('about_us-list')
    context = {
        'about_us':about_us
    }
    return render(request, 'dashboard/about_us/edit.html', context)

@login_required(login_url='dashboard:log_in')
def delete_about_us(request, id):
    models.AboutUs.objects.get(id=id).delete()
    messages.success(request, 'About us muvoffaqiyatli o`chirildi')
    return redirect('dashboard:about_us-list')


""" Contact section """
@login_required(login_url='dashboard:log_in')
def list_contact(request):   
    contacts = models.Contact.objects.all()
    messages.success(request, 'Xabarni ko`rib chiqdingiz')
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
        messages.success(request, 'Xabarni ko`rib chiqdingiz')
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
            messages.success(request, 'Muvoffaqiyatli ro`yxatdan o`tdingiz')
            return redirect('dashboard:log_in')
        elif password != password_confirm:
            messages.error(request, 'Parol bir xil emas')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'Bunday foydalanuvchi mavjud')
            return redirect('dashboard:register')
    return render(request, 'dashboard/auth/register.html')


def log_in(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Xush kelibsiz')
            return redirect('dashboard:index')
            
        else:
            messages.error(request, 'Username yoki parol noto`g`ri')
            return render(request, 'dashboard/auth/login.html')
    else:
        messages.error(request, 'Username yoki parol noto`g`ri')
        return render(request, 'dashboard/auth/login.html')


def log_out(request):
    logout(request)
    return redirect('main:index')


def query(request):
    q = request.GET.get('q')
    banners = models.Banner.objects.filter(title__icontains=q)
    services = models.Service.objects.filter(title__icontains=q)
    prices = models.Price.objects.filter(title__icontains=q)
    contact = models.Contact.objects.filter(title__icontains=q)
    context = {
        'banners': banners,
        'services': services,
        'prices': prices,
        'contact': contact
    }
    return render(request, 'dashboard/query.html', context)