from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .utils.import_records import import_records


@receiver(post_migrate)
def on_startup(sender, **kwargs):
    if sender.name == 'crm':
        import_records()
