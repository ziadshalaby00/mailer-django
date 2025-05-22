
# 📧 mailer - Email Sending Utility for Django Projects

`mailer` is a simple utility function used to send plain text or HTML emails using Django's SMTP configuration. It can be easily integrated into any Django project.

---

## 🧱 Installation

### 1. Add a `utils.py` file to your application, for example:

```
project/
│
├── main_app/
│   ├── views.py
│   ├── utils.py     ← 📍 Contains send_contact_email
│
├── project/      
│   ├── settings.py  ← Email configuration
```

---

## ⚙️ Settings

In your project's `settings.py`, add the following email configuration:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'admin@example.com'         # The sender email address
EMAIL_HOST_PASSWORD = 'your_app_password'     # Gmail app password
```

> 🟡 **Note:** To get an app password from Gmail:
> - Enable two-factor authentication (2FA).
> - Go to your Google account security settings.
> - Generate an app password and use it instead of your regular password.

---

## How to Use

### 1. Call the Send Function

```python
from main_app.utils import send_contact_email

send_contact_email(
    name='Ziad',
    email_recipients=['someone@example.com'],
    message='Hello, this is a test email.',
    html_message='<h1 style="color:blue">This is a test HTML email</h1>'
)
```

### 2. Example in a View

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import send_contact_email

class ContactEmailView(APIView):
    def get(self, request):
        send_contact_email(
            name='Ziad',
            email_recipients=['Ziad@example.com'],
            message='Test email body',
            html_message='<p style="color:red">Test HTML content</p>'
        )
        return Response({"success": "Email sent successfully!"})
```

---

## 📤 About the `send_contact_email` Function

```python
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
```

#### Parameters:
- `name`: The sender's name that appears in the subject.
- `message`: Plain text body of the email.
- `email_recipients`: List of recipient email addresses.
- `html_message` (optional): HTML content of the email.

---

## ✅ Notes

- Make sure your SMTP settings are correct.
- Always test email sending in a safe development environment before using it in production.
- You can extend the function to support attachments or more features.

---

## License

This utility is open source. Feel free to use and modify it in your projects.