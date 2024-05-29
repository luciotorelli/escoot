from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.contrib import messages
from .forms import ContactForm
from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST, user=request.user)
        if form.is_valid():
            contact_message = form.save()
            _send_contact_email(contact_message)
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('contact:contact')
    else:
        form = ContactForm(user=request.user)
    return render(request, 'contact/contact.html', {'form': form})

def _send_contact_email(contact_message):
    """Send the contact email"""
    subject = f'Contact Us Message from {contact_message.name}'
    context = {
        'name': contact_message.name,
        'email': contact_message.email,
        'message': contact_message.message,
    }
    if contact_message.order:
        context['order_number'] = contact_message.order.order_number
    body = render_to_string(
        'contact/contact_email_body.txt',
        context
    )
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        [settings.DEFAULT_FROM_EMAIL]
    )
