from django.urls import path
from .views import HomePageView, ExpensesCreateView, ExpensesUpdateView, ExpensesDeleteView

urlpatterns = [
    path('', HomePageView.as_view(), name='home' ),
    # path('categories/add/', AddCategoryView.as_view(), name='add_category'),
    path('transactions/add/', ExpensesCreateView.as_view(), name='add_transaction'),
    path('transactions/<int:pk>/update/', ExpensesUpdateView.as_view(), name='update_transaction'),
    path('transaction/<int:pk>/delete/',ExpensesDeleteView.as_view(), name='delete_transaction')
    
]