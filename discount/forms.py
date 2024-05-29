from django import forms

class DiscountCodeApplyForm(forms.Form):
    code = forms.CharField(max_length=20, label='Discount Code')