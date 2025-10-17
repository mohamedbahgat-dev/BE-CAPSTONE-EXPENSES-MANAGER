from rest_framework import generics, permissions
from expenses.models import Expense
from .serializers import ExpenseSerializer
from .permissions import IsAuthorOrReadOnly


# Create your views here.
class ExpensesAPIView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthorOrReadOnly]

class ExpensesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthorOrReadOnly]

