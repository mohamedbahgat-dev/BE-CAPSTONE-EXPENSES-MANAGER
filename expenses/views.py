from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import ExpensesForm
from .models import Category, Expense


# Create your views here.
class ExpensesCreateView(CreateView):
    model = Expense
    form_class = ExpensesForm
    template_name = 'transaction/add_transaction.html'
    success_url = reverse_lazy('home')
    context_object_name = 'transactions'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ExpensesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Expense
    form_class = ExpensesForm
    template_name = 'transaction/update_transaction.html'
    success_url = reverse_lazy('home')
    context_object_name = 'transactions'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        """Ensure only the owner of the expense can edit it"""
        expense = self.get_object()
        return self.request.user == expense.user


class ExpensesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Expense
    template_name = 'transaction/delete_transaction.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        """Ensure only the owner of the expense can edit it"""
        expense = self.get_object()
        return self.request.user == expense.user


class HomePageView(ListView):
    model = Expense
    template_name = 'home.html'
    context_object_name = 'transactions'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Expense.objects.filter(user=self.request.user).order_by('-date')
        return Expense.objects.none()


