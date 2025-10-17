from django.contrib import admin
from .models import Expense, Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('name', 'is_default')
    search_fields = ('name',)


class ExpenseAdmin(admin.ModelAdmin):
    model = Expense
    list_display = ('description', 'amount', 'category', 'date', 'user')
    search_fields = ('description', 'category__name')
    list_filter = ('category', 'date')


admin.site.register(Expense)
admin.site.register(Category)
