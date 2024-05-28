from django import forms
from .models import WishlistItem

class AddToWishlistForm(forms.ModelForm):
    class Meta:
        model = WishlistItem
        fields = ['product']

class RemoveFromWishlistForm(forms.ModelForm):
    class Meta:
        model = WishlistItem
        fields = []
