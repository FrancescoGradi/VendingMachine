from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.db.models import Sum, Value, Count
from django.db.models.fields import BooleanField
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from . import servoControl as servo

from .models import CoffeeCapsule, History

def index(request):
    coffee_list = CoffeeCapsule.objects.all().values('coffeeType', 'coffeePrice').annotate(coffeeQuantity=Sum('coffeeQuantity'), firstExpired=Value(False, BooleanField()))
    # Per la scadenza aggiungo un campo firstExpired all'oggetto passato coffee_list, a quel punto con una query
    # identifico il primo elemento di ogni tipo di caffe' (cioe' la prossima capsula erogata) e verifico la
    # scadenza. Se scaduto metto firstExpired a True, così facendo l'html riesce a decidere se dare non
    # disponibile un tipo di capsula

    for capsule in coffee_list:
        if CoffeeCapsule.objects.filter(coffeeType=capsule['coffeeType']).order_by('additionDate')[0].isExpired():
            capsule['firstExpired'] = True

    return render(request, 'coffee/index.html', {'coffee_list': coffee_list})

def payment(request, coffeeType):
    capsules = CoffeeCapsule.objects.filter(coffeeType=coffeeType).order_by('additionDate')
    return render(request, 'coffee/payment.html', {'capsule': capsules[0]})

def about(request):
    return render(request, 'coffee/about.html')

def contact(request):
    return render(request, 'coffee/contact.html')

def registration(request, registrationFailed = False):
    return render(request, 'coffee/registration.html')

def validateUser(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        name = request.POST.get('name')
        lastName = request.POST.get('last_name')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm password')

        if not User.objects.filter(username='username').exists():
            if password == confirm:
                user = User(username=username, first_name=name, last_name=lastName)
                user.set_password(password)
                user.save()
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request, 'coffee/registration.html', {'registrationFailed': True})

        return render(request, 'coffee/registration.html', {'registrationFailed': True})
    else:
        return render(request, 'coffee/registration.html', {'registrationFailed': True})

def pay(request, coffeeType):
    if request.user.is_authenticated:
        user = request.user

        coffee_type_list = CoffeeCapsule.objects.filter(coffeeType=coffeeType)
        coffee_type_list.order_by('additionDate')

        isLast = False
        if len(coffee_type_list) is 1:
            isLast = True

        if coffee_type_list[0].deleteOneCapsule(isLast):

            coffeePrice = 0.50
            if coffeeType == 'Classic':
                coffeePrice = 0.40

            history = History(user=user, hCoffeeType = coffeeType, hCoffeePrice = coffeePrice)
            history.save()

            if coffeeType == 'Classic':
                servo.getCapsule(1)
            else:
                servo.getCapsule(2)

            return render(request, 'coffee/thanksPage.html')

        else:
            return pay(request, coffeeType)
    else:
        return render(request, 'coffee/login.html')

def log(request, loginFailed = False):
    return render(request, 'coffee/login.html', {'loginFailed': loginFailed})

def authenticateView(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))

        else:
            return render(request, 'coffee/login.html', {'loginFailed': True})

@login_required
def account(request):
    user = request.user
    historyList = History.objects.filter(user=user).order_by('-purchaseTime')
    totalSpending = History.objects.filter(user=user).aggregate(total=Sum('hCoffeePrice'))['total']
    favouriteType = historyList.values("hCoffeeType").annotate(coffeeQuantity=Count('hCoffeeType'))[0]

    if totalSpending is not None:
        totalSpending = round(totalSpending, 2)
    else:
        totalSpending = 0

    return render(request, 'coffee/account.html',
                  {'user': user, 'historyList': historyList, 'totalSpending': totalSpending, 'favouriteType': favouriteType['hCoffeeType']})

@login_required
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

@login_required
def cleanHistory(request):
    user = request.user
    historyList = History.objects.filter(user=user)

    for history in historyList:
        history.clean()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))




