from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Expense, Income
from .serializers import Expense_Serializer, Income_Serializer

# Create your views here.
class ExpenseListView(APIView):
    def get(self, request):
        expenses = Expense.objects.all()
        serializer = Expense_Serializer(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class IncomeListView(APIView):
    def get(self, request):
        incomes = Income.objects.all()
        serializer = Income_Serializer(incomes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)