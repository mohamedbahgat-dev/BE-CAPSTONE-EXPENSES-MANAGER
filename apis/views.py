from rest_framework import generics
from expenses.models import Expense
from .serializers import ExpenseSerializer, UserSerializer
from .permissions import IsAuthorOrReadOnly, IsUserOrReadOnly
from django.contrib.auth import get_user_model



# Create your views here.
class ExpensesAPIView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthorOrReadOnly]

class ExpensesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthorOrReadOnly]

class UserListAPIView(generics.ListCreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOrReadOnly]

class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOrReadOnly]