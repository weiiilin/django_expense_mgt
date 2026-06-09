"""專案層級 URL 路由總表。

教學重點：
1. 先在這裡切分「大路由」，再把細節委派給各 app 的 urls.py。
2. `include(...)` 可讓每個 app 自己管理 URL，降低耦合。
3. 建議保持此檔精簡：只放總入口，不放商業邏輯。
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Django 管理後台。
    path('admin/', admin.site.urls),
    # 帳號相關路由（登入、登出、註冊）。
    path('accounts/', include('accounts.urls')),
    # 主要功能路由（Learning Log 主 app）。
    path('', include('learning_logs.urls')),
]
