from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from .models import UserData
from . import forms

# Sign-up page view. Creates a new user/password entry.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:userhome')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', { 'form': form })

# Userhome rendering view - first function. Only accessible to logged-in users.
@login_required(login_url="/accounts/login")
def user_homepage(request):
    return render(request, 'accounts/userhome.html')

# Log-in view. Authenticates user log-in information.
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            return redirect('accounts:userhome')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', { 'form': form })

# Userhome rendering view - second function. Only accessible to logged-in users.
@login_required(login_url="/accounts/login")
def user_homepage(request):
    username = request.user
    context = {
        "Uname": username
    }
    return render(request, 'accounts/userhome.html', context)

# Log-out view. Logs out users.
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('accounts:login')

# NewEntry rendering view. Displays NewEntry form for users to add new entries. Only accessible to logged-in users.
@login_required(login_url="/accounts/login")
def newentry_view(request):
    if request.method == 'POST':
        form = forms.NewEntry(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('accounts:userhome')
    else:
        form = forms.NewEntry()
    return render(request, 'accounts/newentry.html', {'form': form})

# PasswordBank rendering view. Displays user-specific data in the PasswordBank. Only accessible to logged-in users.
@login_required(login_url="/accounts/login")
def userdata_display(request):
    all_accounts = UserData.objects.filter(user=request.user)
    template = loader.get_template('accounts/passwordbank.html')
    context = {
        'all_accounts': all_accounts,
    }
    return HttpResponse(template.render(context, request))

class CleanView(DeleteView):
    model=UserData
    template_name = 'accounts/template.html'
    context_object_name = 'accounts'
    success_url = reverse_lazy('accounts:passwordbank')
