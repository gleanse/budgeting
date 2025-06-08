
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.expense.models import Expense
from apps.expense.v1.serializers import Expense_Serializer


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
