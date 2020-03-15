from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import ContactForm
from .models import ContactUs


def homepage(request):
    return render(request, 'homepage.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')


def useraccount(request):
    return render(request, 'useraccount.html')


def contact(request):
    template_name = 'contact.html'
    if request.method == "POST":
        form = ContactForm(request.POST or None)
        errors = None
        if form.is_valid():
            ContactUs.objects.create(
                name = form.cleaned_data.get('name'),
                email = form.cleaned_data.get('email'),
                phone = form.cleaned_data.get('phone'),
                message = form.cleaned_data.get('message'),
                created_at = form.cleaned_data.get('created_at')
            )
            return HttpResponseRedirect("/login/")
        if form.errors:
            errors = form.errors

        context = {"form": form, "errors": errors}
        return render(request, template_name, context)
    else:
        form = ContactForm()
        return render(request, template_name, {'form':form})