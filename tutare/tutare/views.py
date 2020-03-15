from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import UserAccount

def homepage(request):
    return render(request, 'homepage.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def useraccount(request):
    all_accounts = UserAccount.objects.all()
    template = loader.get_template('useraccount.html')
    context = {
        'all_accounts': all_accounts,
    }
    return HttpResponse(template.render(context, request))
