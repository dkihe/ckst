from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import loader

# from .forms import ContactForm
# from .models import ContactUs, UserAccount


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')
