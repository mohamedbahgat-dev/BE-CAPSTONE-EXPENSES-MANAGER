from django.urls import path
from .views import ExpensesAPIView, ExpensesDetailAPIView

urlpatterns = [
    path("expenses/", ExpensesAPIView.as_view(), name='expense_list'),
    path("expense/<int:pk>/", ExpensesDetailAPIView.as_view(), name='expense_detail')
]