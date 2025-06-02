from rest_framework import serializers
from .models import Expense, Income

class Expense_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = '__all__'

class Income_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Income
        fields = '__all__'