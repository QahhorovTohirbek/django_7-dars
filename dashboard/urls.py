from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.users_list, name='users'),

    # banner
    path('banner-list/', views.list_banner, name='banner-list'),
    path('banner-create/', views.create_banner, name='banner-create'),
    path('banner-detail/<int:id>/', views.detail_banner, name='banner-detail'),
    path('banner-edit/<int:id>/', views.edit_banner, name='banner-edit'),
    path('banner-delete/<int:id>/', views.delete_banner, name='banner-delete'),

    # service
    path('service-list/', views.list_service, name='service-list'),
    path('service-create/', views.create_service, name='service-create'),
    path('service-detail/<int:id>/', views.detail_service, name='service-detail'),
    path('service-edit/<int:id>/', views.edit_service, name='service-edit'),
    path('service-delete/<int:id>/', views.delete_service, name='service-delete'),

    #price
    path('price-list/', views.list_price, name='price-list'),
    path('price-create/', views.create_price, name='price-create'),
    path('price-detail/<int:id>/', views.detail_price, name='price-detail'),
    path('price-edit/<int:id>/', views.edit_price, name='price-edit'),
    path('price-delete/<int:id>/', views.delete_price, name='price-delete'),

    # about_us
    path('about_us-list/', views.list_about_us, name='about_us-list'),
    path('about_us-create/', views.create_about_us, name='about_us-create'),
    path('about_us-detail/<int:id>/', views.detail_about_us, name='about_us-detail'),
    path('about_us-edit/<int:id>/', views.edit_about_us, name='about_us-edit'),
    path('about_us-delete/<int:id>/', views.delete_about_us, name='about_us-delete'),

    # contact
    path('contact-list/', views.list_contact, name='contact-list'),
    path ('contact-detail/<int:id>/', views.detail_contact, name='contact-detail'),
    path('contact-edit/<int:id>/', views.edit_contact, name='contact-edit'),

    # Register login

    path('register/', views.register, name='register'),
    path('log-in/', views.log_in, name='log_in'),
    path('log-out/', views.log_out, name='log_out'),
]