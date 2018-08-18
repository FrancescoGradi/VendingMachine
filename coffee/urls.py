from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:coffeeCapsule_id>/payment/', views.payment, name='payment'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('payment/pay/', views.pay, name='pay'),
]