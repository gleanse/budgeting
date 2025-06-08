from django.urls import path
from apps.expense.v1.views import ExpenseListView

urlpatterns = [
    path('expenses/', ExpenseListView.as_view(), name='expense-list'),
]