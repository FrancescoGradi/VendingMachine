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
        return CoffeeCapsule.objects.order_by('additionDate')[0:5]

def index(request):
    return render(request, 'coffee/index.html')

def about(request):
    return render(request, 'coffee/about.html')

def contact(request):
    return render(request, 'coffee/contact.html')

#def getData(request, varToGet):
