
from rest_framework import serializers
from apps.expense.models import Expense


class Expense_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'
