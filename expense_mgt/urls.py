from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import BootstrapLoginForm

app_name = 'expense_mgt'

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html', authentication_form=BootstrapLoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='expense_mgt:login'), name='logout'),
    path('expenses/<int:pk>/edit/', views.expense_edit, name='edit'),
    path('testapi/', views.test_api, name='test_api'),
]