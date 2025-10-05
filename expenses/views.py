from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import CategoryForm
from .models import Category

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'home.html'


class AddCategoryView(LoginRequiredMixin, FormView):
    template_name = 'categories/add_category.html'
    form_class = CategoryForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        category_choice = form.cleaned_data['category_choice']
        custom_category = form.cleaned_data['custom_category']

        if category_choice == 'custom':
            category_name = custom_category
            is_predefined = False
            user = self.request.user
        else:
            category_name = category_choice
            is_predefined = True
            user = None

        category, created = Category.objects.get_or_create(
            name = category_name,
            user = user,
            defaults={'is_predefined': is_predefined}
        )

        if created:
            messages.success(self.request, f"Category '{category_name}' added successfully.")
        else:
            messages.info(self.request, f"Category '{category_name}' already exists.")


        return super().form_valid(form)

