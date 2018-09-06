from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('registration/validateUser', views.validateUser, name='validateUser'),
    path('<str:coffeeType>/payment/', views.payment, name='payment'),
    path('<str:coffeeType>/payment/pay/', views.pay, name='pay'),
    path('login/', views.log, name='log'),
    path('login/authenticate/', views.authenticateView, name='authenticate'),
    path('logout/', views.logoutView, name='logout'),
    path('account/', views.account, name='account'),
    path('account/clean', views.cleanHistory, name='cleanHistory'),
    path('finish/', views.finish, name='finish'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]