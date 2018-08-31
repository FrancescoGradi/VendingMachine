from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import Sum
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from .models import CoffeeCapsule

class IndexView(generic.ListView):
    template_name = 'coffee/index.html'
    context_object_name = 'coffee_list'

    # Ritorna la lista dei caffe', raggruppata in base al tipo, con quantità sommate
    def get_queryset(self):
        return CoffeeCapsule.objects.all().values('coffeeType', 'coffeePrice').annotate(coffeeQuantity=Sum('coffeeQuantity'))

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

def registration(request, registrationFailed = False):
    return render(request, 'coffee/registration.html')

def validateUser(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        name = request.POST.get('name')
        lastName = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm password')

        print(username + name + lastName + password)

        print

        if not User.objects.filter(username='username').exists():
            if password == confirm:
                user, created = User.objects.get_or_create(username=username, first_name=name, last_name=lastName, password=password)
                if created:
                    user.save()
                    return HttpResponseRedirect(reverse('index'))
                else:
                     return render(request, 'coffee/registration.html', {'registrationFailed': True})

        return render(request, 'coffee/registration.html', {'registrationFailed': True})
    else:
        return render(request, 'coffee/error.html')

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