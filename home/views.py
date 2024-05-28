from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsletterSignUpForm
from .mailchimp_utils import subscribe_email

def index(request):
    """ A view to return the index page """
    form = NewsletterSignUpForm()
    if request.method == "POST":
        form = NewsletterSignUpForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            result = subscribe_email(email)
            if 'status' in result and result['status'] == 'pending':
                messages.success(request, 'Thank you for signing up! Please check your email to confirm your subscription.')
            else:
                messages.error(request, f"An error occurred: {result.get('message', 'Unknown error')}")
            return redirect('home')
    return render(request, 'home/index.html', {'form': form})
