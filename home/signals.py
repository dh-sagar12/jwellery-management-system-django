from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import FeatureProductModel

@receiver(post_save, sender=FeatureProductModel)
def set_single_main(sender, instance, created, **kwargs):
    if created:
        FeatureProductModel.objects.set_single_main(instance)
