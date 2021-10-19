from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):  # *args, **kwargs
    print(args, kwargs)  # (<WSGIRequest: GET '/'>,) {}
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact</h1>")  # string of HTMl code


def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>About</h1>")


def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social</h1>")
