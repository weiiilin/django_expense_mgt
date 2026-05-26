from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'expense_mgt'

urlpatterns = [
    # 設定根目錄路徑指向 home 視圖
    path('', views.home, name='home'),
    path('api/add/', views.api_add_expense, name='api_add_expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete'),

    # 使用 Django 內建的登入/登出視圖
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='expense_mgt:login'), name='logout'),
]