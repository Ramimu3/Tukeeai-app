from ninja import NinjaAPI
from .models import UserPayment
from .schemas import UserPaymentSchema
import stripe
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.middleware.csrf import get_token
from django.http import JsonResponse

stripe_router = NinjaAPI(urls_namespace='stripe_router')

@stripe_router.get('/user-payment', response=UserPaymentSchema)
def get_user_payment(request):
    user_payment = UserPayment.objects.filter(user=request.user).first()
    return user_payment
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@stripe_router.post('/create-checkout-session')
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
        response = JsonResponse({'checkout_url': checkout_session.url})
        response['X-CSRFToken'] = get_token(request)
        return response
    except stripe.error.StripeError as e:
        return JsonResponse({'error': str(e)}, status=400)
    

@stripe_router.get('/payment-details/{session_id}')
def get_payment_details(request, session_id: str):
    user_payment = get_object_or_404(UserPayment, stripe_checkout_id=session_id)
    # Retrieve payment details from Stripe API or your database
    payment_details = {
        'amount': user_payment.amount,
        'currency': user_payment.currency,
        'payment_method': user_payment.payment_method,
        # Add other relevant payment details
    }
    return payment_details

@stripe_router.get('/csrf-token')
def get_csrf_token(request):
    return {'csrfToken': get_token(request)}