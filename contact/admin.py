from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_submitted', 'order')
    list_filter = ('date_submitted', 'order')
    search_fields = ('name', 'email', 'message')

admin.site.register(ContactMessage, ContactMessageAdmin)
