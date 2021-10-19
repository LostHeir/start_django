from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):  # *args, **kwargs
    print(args, kwargs)  # (<WSGIRequest: GET '/'>,) {}
    return HttpResponse("<h1>Hello World</h1>")  # string of HTMl code


def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact</h1>")


def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>About</h1>")


def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social</h1>")
