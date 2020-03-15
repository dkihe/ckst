from django.http import HttpResponse
from django.shortcuts import render

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
    context = {
        'all_accounts': all_accounts,
    }
    return render(request, 'useraccount.html')
