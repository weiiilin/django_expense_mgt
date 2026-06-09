from django.urls import path

from .api_views import ExpenseRecordDetailAPIView, ExpenseRecordListCreateAPIView

app_name = 'expense_api'

urlpatterns = [
    path('expenses/', ExpenseRecordListCreateAPIView.as_view(), name='expense-list'),
    path('expenses/<int:pk>/', ExpenseRecordDetailAPIView.as_view(), name='expense-detail'),
]