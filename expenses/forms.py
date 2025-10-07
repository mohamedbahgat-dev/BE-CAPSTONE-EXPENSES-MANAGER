from django import forms
from .models import Category

class CategoryForm(forms.Form):
    CATEGORY_CHOICES = Category.PREDEFINED_CHOICES + [('custom','Other / Custom')]

    category_choice = forms.ChoiceField(
        choices=[('', '--- Choose Category ---')] + CATEGORY_CHOICES,
        label='Category',
        required=True
    )
    custom_category = forms.CharField(
        max_length=50,
        required=False,
        label='Custom Category'
    )

    def clean(self):
        cleaned_data = super().clean()
        category_choice = cleaned_data.get('category_choice')
        custom_category = cleaned_data.get('custom_category')
        if category_choice == 'custom' and not custom_category:
            raise forms.ValidationError('Please enter a custom category name')
        return cleaned_data