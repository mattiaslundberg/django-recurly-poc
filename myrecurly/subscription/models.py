from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from myrecurly.utils import recurly

@receiver(post_save, sender = User)
def create_recurly_account(sender, instance, created, *args, **kwargs):
    if created:
        account = recurly.Account(account_code = instance.id)
    else:
        # TODO: This will break if we don't have an account created
        account = recurly.Account.get(instance.id)
    account.first_name = instance.first_name
    account.last_name = instance.last_name
    account.email = instance.email
    account.save()
