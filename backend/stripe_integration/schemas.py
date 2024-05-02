# stripe_integration/schemas.py
from ninja import Schema

class UserPaymentSchema(Schema):
    id: int
    user_id: int
    stripe_checkout_id: str
    # Add other relevant fields
