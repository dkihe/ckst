from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.contrib import messages

def contact_us(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{0} has sent you a new message:\n\n{1}".format(sender_name, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['sabineshawaii.edu'])
            messages.success(request, 'Thanks for contacting us!')
            return redirect('accounts:userhome')
    else:
        form = ContactForm()
    return render(request, 'contactus/contactus.html', {'form': form})
