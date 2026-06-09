"""learning_logs app 的 URL 規則。"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 首頁。
    path('', views.index, name='index'),
    # 主題列表頁。
    path('topics/', views.topics, name='topics'),
    # 單一主題詳情頁。
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 新增主題頁。
    path('new_topic/', views.new_topic, name='new_topic'),
    # 新增筆記頁。
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # 編輯筆記頁。
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]