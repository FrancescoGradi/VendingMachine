from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('registration/', views.registration, name='registration'),
    path('registration/validateUser', views.validateUser, name='validateUser'),
    path('<str:coffeeType>/payment/', views.payment, name='payment'),
    path('<str:coffeeType>/payment/login', views.loginPage, name='loginPage'),
    path('<str:coffeeType>/payment/pay/', views.pay, name='pay'),
    path('<str:coffeeType>/payment/pay/error', views.errorPage, name='errorPage'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]