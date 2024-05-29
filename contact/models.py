from django.db import models
from django.conf import settings
from checkout.models import Order

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='contact_messages')
    date_submitted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.name} on {self.date_submitted}'
