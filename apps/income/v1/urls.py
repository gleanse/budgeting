from django.urls import path
from apps.income.v1.views import IncomeListView


urlpatterns = [
    path('incomes/', IncomeListView.as_view(), name='income-list'),
]