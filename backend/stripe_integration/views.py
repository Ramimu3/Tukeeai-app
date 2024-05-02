from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.conf import settings
from .models import UserPayment
import stripe
import time
from ninja import NinjaAPI
from django.http import JsonResponse

stripe_api = NinjaAPI(title='Stripe Integration API', urls_namespace='stripe_api')

@login_required(login_url='login')
def product_page(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    if request.method == 'POST':
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': settings.PRODUCT_PRICE,
                    'quantity': 1,
                },
            ],
            mode='payment',
            customer_creation='always',
            success_url=settings.REDIRECT_DOMAIN + '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.REDIRECT_DOMAIN + '/payment_cancelled',
        )
        return redirect(checkout_session.url, code=303)
    return render(request, 'stripe_integration/product_page.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserPayment
import stripe
from django.conf import settings
from django.middleware.csrf import get_token

@login_required
def payment_successful(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    checkout_session_id = request.GET.get('session_id')
    
    if checkout_session_id:
        try:
            session = stripe.checkout.Session.retrieve(checkout_session_id)
            customer = stripe.Customer.retrieve(session.customer)
            
            # Retrieve the UserPayment object or create a new one
            user_payment, created = UserPayment.objects.get_or_create(
                user=request.user,
                defaults={
                    'stripe_checkout_id': checkout_session_id,
                    # Set other relevant fields
                }
            )
            
            if not created:
                # Update the existing UserPayment object
                user_payment.stripe_checkout_id = checkout_session_id
                # Update other relevant fields
                user_payment.save()
            
            # Process the successful payment
            # ...
            
            return render(request, 'stripe_integration/payment_successful.html', {'customer': customer})
        
        except stripe.error.StripeError as e:
            # Handle Stripe-related errors
            error_message = str(e)
            return render(request, 'stripe_integration/payment_error.html', {'error_message': error_message})
    
    else:
        # Handle missing session_id parameter
        error_message = "Missing session_id parameter."
    return JsonResponse({'success': True})

def payment_cancelled(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    return JsonResponse({'success': False})




@csrf_exempt
def stripe_webhook(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    time.sleep(10)
    payload = request.body
    signature_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None
    try:
        event = stripe.Webhook.construct_event(
            payload, signature_header, settings.STRIPE_WEBHOOK_SECRET_TEST
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        session_id = session.get('id', None)
        time.sleep(15)
        user_payment = UserPayment.objects.get(stripe_checkout_id=session_id)
        user_payment.payment_status = True
        user_payment.save()
    return HttpResponse(status=200)
from django.urls import reverse
def stripe_checkout(request):
    if request.method == 'POST':
        stripe.api_key = settings.STRIPE_SECRET_KEY
        session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': settings.STRIPE_SUBSCRIPTION_PRICE_ID,
                'quantity': 1,
            }],
            mode='subscription',
            client_reference_id=request.user.id if request.user.is_authenticated else None,
            success_url=request.build_absolute_uri(reverse('payment_successful')) + f'?session_id={"{CHECKOUT_SESSION_ID}"}',
            cancel_url=request.build_absolute_uri(reverse('payment_cancelled')),
        )
        return redirect(session.url, code=303)

@stripe_api.post('/create-checkout-session/')
def create_checkout_session(request):
    stripe.api_key = settings.STRIPE_SECRET_KEY
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': 'price_1P6jxQA550ilgONrmCpAbYyx',  # Replace with your actual price ID
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='http://localhost:8000/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url='http://localhost:8000/cancel',
        )
        return JsonResponse({'checkout_url': checkout_session.url})
    except stripe.error.StripeError as e:
        return JsonResponse({'error': str(e)}, status=400)