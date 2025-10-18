from django.urls import path
from .views import HomePageView, ExpensesCreateView, ExpensesUpdateView, ExpensesDeleteView, DashboardView

urlpatterns = [
    path('', HomePageView.as_view(), name='home' ),
    path('Dashboard/<int:pk>/', DashboardView.as_view(), name='dashboard' ),
    path('transactions/add/', ExpensesCreateView.as_view(), name='add_transaction'),
    path('transactions/<int:pk>/update/', ExpensesUpdateView.as_view(), name='update_transaction'),
    path('transaction/<int:pk>/delete/',ExpensesDeleteView.as_view(), name='delete_transaction')
    
]