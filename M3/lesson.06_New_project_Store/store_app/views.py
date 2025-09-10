from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello world!</h1>")


def about(request):
    return HttpResponse("<h1>О нас</h1>")


def contact(request):
    return HttpResponse("<h1>Контакты</h1>")