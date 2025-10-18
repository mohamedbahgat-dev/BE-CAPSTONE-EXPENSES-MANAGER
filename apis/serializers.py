from rest_framework import serializers
from expenses.models import Expense
from django.contrib.auth import get_user_model

User = get_user_model()


class ExpenseSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only = True)

    class Meta:
        model = Expense
        fields = (
            'id',
            'user',
            'amount',
            'description',
            'date',
            'category',
            'category_name',
        )

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id','username','email','is_superuser','is_staff','first_name','last_name','age','last_login','location','language','currency','date_joined')