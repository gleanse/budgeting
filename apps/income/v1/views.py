from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.income.models import Income
from apps.income.v1.serializers import Income_Serializer


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