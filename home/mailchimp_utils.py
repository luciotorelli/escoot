import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from django.conf import settings
import requests

def subscribe_email(email):
    client = MailchimpMarketing.Client()
    client.set_config({
        "api_key": settings.MAILCHIMP_API_KEY,
        "server": "us22"
    })
    try:
        response = client.lists.add_list_member(settings.MAILCHIMP_LIST_ID, {
            "email_address": email,
            "status": "pending"
        })
        return response
    except ApiClientError as error:
        error_response = error.text
        if "is already a list member" in error_response:
            return {'status': 'error', 'message': 'This email is already subscribed.'}
        return {'status': 'error', 'message': str(error)}
    except requests.exceptions.ConnectionError as error:
        return {'status': 'error', 'message': 'Connection error occurred. Please try again later.'}
