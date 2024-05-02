from django.urls import path, include
from .views import stripe_api, product_page, payment_successful, payment_cancelled, stripe_webhook, stripe_checkout, create_checkout_session
from .api import stripe_router
from .csrf_token import get_csrf_token

urlpatterns = [
    path('product/', product_page, name='product_page'),
    path('payment-successful/', payment_successful, name='payment_successful'),
    path('payment-cancelled/', payment_cancelled, name='payment_cancelled'),
    path('webhook/', stripe_webhook, name='stripe_webhook'),
    path('api/', stripe_api.urls),

]
