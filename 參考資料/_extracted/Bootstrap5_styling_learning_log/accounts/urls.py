"""accounts app 的 URL 規則。"""

from django.urls import path, include

from . import views


app_name = 'accounts'
urlpatterns = [
    # 載入 Django 內建認證路由：login、logout、password reset...等。
    path('', include('django.contrib.auth.urls')),
    # 自訂註冊頁。
    path('register/', views.register, name='register'),
]