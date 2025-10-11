from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Category

@receiver(post_migrate)
def create_default_categories(sender, **kwargs):

    default_categories = ['Food','Utilities','Healthcare', 'Transport' ,'Rent','Entertainment','Other']
    for cat in default_categories:
        Category.objects.get_or_create(name = cat, is_default=True)
