from django.urls import path
from .views import ExpenseListView, IncomeListView

urlpatterns = [
    path('expenses/', ExpenseListView.as_view(), name='expense-list'),
    path('incomes/',IncomeListView.as_view(), name='incomes-list')
]
