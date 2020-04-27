from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template import loader

# from .forms import ContactForm
# from .models import ContactUs, UserAccount

# Renders the front Homepage of the site.
def homepage(request):
    return render(request, 'homepage.html')

# Renders the About page of the site.
def about(request):
    return render(request, 'about.html')
