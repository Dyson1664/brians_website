from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import ContactForm
import logging

logger = logging.getLogger(__name__)

def index(request):
    form = ContactForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            logger.debug(f"Received contact form: {name}, {email}, {subject}, {message}")

            try:
                full_message = f"From: {name} <{email}>\n\nSubject: {subject}\n\nMessage:\n{message}"
                email_message = EmailMessage(
                    subject,
                    full_message,
                    email,  # Sender's email
                    ['dave.reilly@cec.com.vn'],  # Your email
                    headers={'Reply-To': email}  # Set reply-to to the sender's email
                )
                email_message.send(fail_silently=False)
                messages.success(request,
                                 'Your message has been sent successfully.<br>Brian will get in touch with you soon!')
                logger.debug("Email sent successfully")
                return redirect('sent')  # Redirect to a different URL
            except Exception as e:
                messages.error(request, 'An error occurred while sending your message. Please try again later.')
                logger.error(f"Error sending email: {e}")


        else:
            # Form is invalid, do not redirect; instead, re-render the form with errors
            messages.error(request, 'There were errors with your submission. Please correct them and try again.')
            return render(request, 'index.html', {'form': form})  # Stay on the

    return render(request, 'index.html', {'form': form})

def sent(request):
    return render(request, 'sent.html')
