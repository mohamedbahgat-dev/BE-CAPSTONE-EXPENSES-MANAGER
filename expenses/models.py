from django.db import models
from django.contrib.auth import get_user_model
from datetime import date

# get the custom user model
User = get_user_model()

# Create your models here.
# create category model with predefined category names and option for user to add a custom category
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    is_default = models.BooleanField(default=False)
    
    class Meta:
        verbose_name_plural = 'Caregories'
        ordering = ['name']

    def __str__(self):
        return self.name


# create Expense model with foreign keys of user and category
class Expense(models.Model): 
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=250, blank=True)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='expenses'
    )
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        return f"{self.category} - {self.amount} at {self.date}"
    

# budget model creation with foreign key for user and predefined choices for month, also defaulted value for year
class Budget(models.Model):
    MONTH_CHOICES = [
        (1, "January"), (2, "February"), (3, "March"), (4, "April"),
        (5, "May"), (6, "June"), (7, "July"), (8, "August"),
        (9, "September"), (10, "October"), (11, "November"), (12, "December"),
    ]
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='budgets'
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    month = models.PositiveSmallIntegerField(choices=MONTH_CHOICES)
    year = models.PositiveIntegerField(default=date.today().year)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "month", "year")
        ordering = ["-year", "-month"]

    def __str__(self):
        return f"{self.month} {self.year} - {self.amount}"
