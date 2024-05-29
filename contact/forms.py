from django import forms
from checkout.models import Order
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    order = forms.ModelChoiceField(queryset=Order.objects.none(), required=False, label="Order (if applicable)")

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message', 'order']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ContactForm, self).__init__(*args, **kwargs)
        if user and user.is_authenticated:
            self.fields['order'].queryset = Order.objects.filter(user_profile__user=user)
