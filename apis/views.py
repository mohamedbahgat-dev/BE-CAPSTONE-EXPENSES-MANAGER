from rest_framework import generics
from expenses.models import Expense
from .serializers import ExpenseSerializer

# Create your views here.
class ExpensesAPIView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

class ExpensesDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer

