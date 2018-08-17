from django.shortcuts import render
from django.http import HttpResponse

# Semplice esempio
def index(request):
    return render(request, 'coffee/index.html')

def about(request):
    return render(request, 'coffee/about.html')

def contact(request):
    return render(request, 'coffee/contact.html')
