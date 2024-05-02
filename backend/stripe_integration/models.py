from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()

class UserPayment(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    payment_status = models.BooleanField(default=False)
    stripe_checkout_id = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Payment"

@receiver(post_save, sender=User)
def create_user_payment(sender, instance, created, **kwargs):
    if created:
        UserPayment.objects.create(user=instance)
