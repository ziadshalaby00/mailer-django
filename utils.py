# mailer/utils.py

from django.core.mail import send_mail
from django.conf import settings

def send_contact_email(name, message, email_recipients, html_message=None):
    subject = f"New Message from {name}"
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=email_recipients,
        fail_silently=False,
        html_message=html_message,
    )