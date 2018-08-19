from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import CoffeeCapsule

# Semplice esempio

class IndexView(generic.ListView):
    template_name = 'coffee/index.html'
    context_object_name = 'coffee_list'

    # Ritorna la lista dei caffe'
    def get_queryset(self):
        return CoffeeCapsule.objects.order_by('additionDate')[0:]

'''class PaymentView(generic.ListView):
    template_name = 'coffee/payment.html'
    context_object_name = 'coffee_list'

    def get_queryset(self):
        return CoffeeCapsule.objects.order_by('additionDate')[0:]
'''

def payment(request, coffeeCapsule_id):
    capsule = get_object_or_404(CoffeeCapsule, pk=coffeeCapsule_id)
    return render(request, 'coffee/payment.html', {'capsule': capsule})

def about(request):
    return render(request, 'coffee/about.html')

def contact(request):
    return render(request, 'coffee/contact.html')

def pay(request):
    # cancella un elemento del database
    if request.method == 'POST':
        coffee_type = request.POST.get('coffeeType')
        print (coffee_type)

        coffee_type_list = CoffeeCapsule.objects.filter(coffeeType=coffee_type)
        coffee_type_list.order_by('additionDate')
        coffee_type_list[0].delete()

        # TODO il codice per far funzionare i motori dovrebbe essere inserito qui
        print ("Crick Crick Crick")

    return HttpResponseRedirect(reverse('index'))
