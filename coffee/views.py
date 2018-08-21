from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import Count
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import CoffeeCapsule

'''
class IndexView(generic.ListView):
    template_name = 'coffee/index.html'
    context_object_name = 'coffee_list'

    # Ritorna la lista dei caffe'
    def get_queryset(self):
        return CoffeeCapsule.objects.order_by('additionDate')[0:]
'''
class IndexView(generic.ListView):
    template_name = 'coffee/index.html'
    context_object_name = 'coffee_list'

    # Ritorna la lista dei caffe'
    def get_queryset(self):
        return CoffeeCapsule.objects.values('coffeeType').annotate(quantity=Count('coffeeType'))

def payment(request, coffeeType):
    capsules = CoffeeCapsule.objects.filter(coffeeType=coffeeType).order_by('additionDate')
    return render(request, 'coffee/payment.html', {'capsule': capsules[0]})

def about(request):
    return render(request, 'coffee/about.html')

def contact(request):
    return render(request, 'coffee/contact.html')

def errorPage(request):
    return render(request, 'coffee/error.html')

def loginPage(request, coffeeType):
    return render(request, 'coffee/login.html', {'coffeeType': coffeeType})

def pay(request, coffeeType):
    username = request.POST.get('user')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if request.method == 'POST':

            coffee_type_list = CoffeeCapsule.objects.filter(coffeeType=coffeeType)
            coffee_type_list.order_by('additionDate')

            if coffee_type_list[0].deleteOneCapsule():

                # TODO il codice per far funzionare i motori dovrebbe essere inserito qui
                print("Crick Crick Crick")

                return HttpResponseRedirect(reverse('index'))

            else:
                print("Quantity error.")
                return HttpResponseRedirect(reverse('errorPage'))
    else:
        return HttpResponseRedirect(reverse('errorPage'))




