from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.
class Category(models.Model):
    PREDEFINED_CHOICES = [
        ('FOOD', 'FOOD'),
        ('Utilities', 'Utilities'),
        ('Healthcare', 'Healthcare'),
        ('Transport', 'Transport'),
        ('Rent', 'Rent'),
        ('Entertainment', 'Entertainment'),
        ('Other', 'Other'),
    ]

    name = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='categories')
    is_predefined = models.BooleanField(default=False)

    class Meta:
        unique_together = ('name', 'user')

    def __str__(self):
        return self.name



