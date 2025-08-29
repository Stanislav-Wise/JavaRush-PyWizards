from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h1>Hello, world.</h1> <p>You're at the polls index.</p>")


def about(request):
    return HttpResponse("<h1>Hello, about.</h1> <p>You're at the polls index.</p>")