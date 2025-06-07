from django.urls import path
from .views import ExpenseListView, IncomeListView, TotalMoneyView, UsersView

urlpatterns = [
    path('registration/',UsersView.as_view(), name='user-register'),
    path('expenses/', ExpenseListView.as_view(), name='expense-list'),
    path('incomes/', IncomeListView.as_view(), name='income-list'),
    path('money/', TotalMoneyView.as_view(), name='total-money'),
]