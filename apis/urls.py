from django.urls import path
from .views import ExpensesAPIView, ExpensesDetailAPIView, UserListAPIView, UserDetailAPIView, CustomRegisterView


urlpatterns = [
    path("expenses/", ExpensesAPIView.as_view(), name='expense_list'),
    path("expenses/<int:pk>/", ExpensesDetailAPIView.as_view(), name='expense_detail'),
    path("users/", UserListAPIView.as_view(), name='user_list'),
    path("users/<int:pk>/", UserDetailAPIView.as_view(), name='user_detail'),
    path("auth/register/", CustomRegisterView.as_view(), name = 'api_register')

]