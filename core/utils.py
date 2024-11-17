from django.core.mail import send_mail
from django.conf import settings

def send_email_notification(subject, message, recipient_list):
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipient_list,
        )
    except Exception as e:
        print(f"Error sending email: {e}")
