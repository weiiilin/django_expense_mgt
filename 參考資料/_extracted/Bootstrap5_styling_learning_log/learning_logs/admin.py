from django.contrib import admin

from .models import Topic, Entry


# 註冊模型到 Django admin，方便後台檢視與維護資料。
admin.site.register(Topic)
admin.site.register(Entry)