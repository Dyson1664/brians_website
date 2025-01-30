from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import ContactForm
import logging
import stripe

from django.conf import settings
from django.shortcuts import redirect
from django.views import View
from django.http import JsonResponse

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
                    ['brianreillyhealth@gmail.com'],  # Your email
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


stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        YOUR_DOMAIN = "http://127.0.0.1:8000"  # Adjust based on your domain

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'eur',
                            'product_data': {
                                'name': 'call',
                            },
                            'unit_amount': 2000,  # 20.00 USD
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=YOUR_DOMAIN + '/success/',
                cancel_url=YOUR_DOMAIN + '/cancel/',
            )
            return redirect(checkout_session.url, code=303)
        except Exception as e:
            return JsonResponse({'error': str(e)})

