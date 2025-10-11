from django import forms
from .models import Category, Expense
    

class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'description','category']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all().order_by('name')
       