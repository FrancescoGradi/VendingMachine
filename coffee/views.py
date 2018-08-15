from django.shortcuts import render
from django.http import HttpResponse

# Semplice esempio
def index(request):
    return HttpResponse("Do you need a cup of coffee?")