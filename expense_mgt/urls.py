from django.urls import path
from . import views

app_name = 'expense_mgt'

urlpatterns = [
    # 設定根目錄路徑指向 home 視圖
    path('', views.home, name='home'),
    path('api/add/', views.api_add_expense, name='api_add_expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete'),
]