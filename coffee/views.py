from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import Sum
from django.contrib.auth import authenticate, login

from .models import CoffeeCapsule

class IndexView(generic.ListView):
    template_name = 'coffee/index.html'
    context_object_name = 'coffee_list'

    # Ritorna la lista dei caffe', raggruppata in base al tipo, con quantità sommate
    def get_queryset(self):
        return CoffeeCapsule.objects.all().values('coffeeType').annotate(coffeeQuantity=Sum('coffeeQuantity'))

def payment(request, coffeeType):
    capsules = CoffeeCapsule.objects.filter(coffeeType=coffeeType).order_by('additionDate')
    return render(request, 'coffee/payment.html', {'capsule': capsules[0]})

def about(request):
    return render(request, 'coffee/about.html')

def contact(request):
    return render(request, 'coffee/contact.html')

def errorPage(request):
    return render(request, 'coffee/error.html')

def loginPage(request, coffeeType, loginFailed = False):
    return render(request, 'coffee/login.html', {'coffeeType': coffeeType, 'loginFailed': loginFailed})

def pay(request, coffeeType):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            coffee_type_list = CoffeeCapsule.objects.filter(coffeeType=coffeeType)
            coffee_type_list.order_by('additionDate')

            isLast = False
            if len(coffee_type_list) is 1:
                isLast = True

            if coffee_type_list[0].deleteOneCapsule(isLast):

                # TODO il codice per far funzionare i motori dovrebbe essere inserito qui
                print("Crick Crick Crick")

                return render(request, 'coffee/erogation.html')

            else:
                return pay(request, coffeeType)
        else:
            return render(request, 'coffee/login.html', {'coffeeType': coffeeType, 'loginFailed': True})

'''def erogation(request, coffeeType):
    # In futuro potrebbe anche rendere il tempo previsto
    return render(request, 'coffee/erogation.html')'''
