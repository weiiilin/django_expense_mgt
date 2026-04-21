from django.contrib import admin
from .models import ExpenseRecord

@admin.register(ExpenseRecord)
class ExpenseRecordAdmin(admin.ModelAdmin):
    # 設定後台列表要顯示的欄位
    list_display = ('created_at', 'category', 'amount', 'description')
    # 設定可以過濾的欄位
    list_filter = ('category', 'created_at')
    # 設定搜尋欄位
    search_fields = ('category', 'description')