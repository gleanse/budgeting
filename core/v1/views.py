from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from core.models import Expense, Income, Money
from .serializers import Expense_Serializer, Income_Serializer, Money_Serializer, User_Serializer


class UsersView(APIView):
    def post(self, request):
        serializer = User_Serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpenseListView(APIView):
    def get(self, request):
        expenses = Expense.objects.all()
        serializer = Expense_Serializer(expenses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Expense_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class IncomeListView(APIView):
    def get(self, request):
        incomes = Income.objects.all()
        serializer = Income_Serializer(incomes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = Income_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TotalMoneyView(APIView):
    def get(self,request):
        total_amount = Money.objects.all()
        serializer = Money_Serializer(total_amount, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)