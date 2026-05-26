from django.contrib import admin
from .models import ExpenseRecord

@admin.register(ExpenseRecord)
class ExpenseRecordAdmin(admin.ModelAdmin):
    # 在 ExpenseRecordAdmin 類別內加入
    def save_model(self, request, obj, form, change):
        if not obj.user:
            obj.user = request.user
        super().save_model(request, obj, form, change)
    # 1. 自訂列表顯示欄位 (在清單頁面看到的欄位)
    list_display = ('date', 'category', 'amount', 'user', 'description')
    
    # 2. 右側篩選過濾功能 (方便依分類、日期、使用者快速篩選)
    list_filter = ('date', 'category', 'user')
    
    # 3. 搜尋功能 (可依備註內容或類別名稱搜尋)
    search_fields = ('description', 'category')
    
    # 4. 預設排序 (依日期由新到舊排序)
    ordering = ('-date',)
    
    # 5. 分頁功能 (每頁顯示 20 筆，防止資料太多載入過慢)
    list_per_page = 20

    # 6. 進階：讓管理員可以直接在列表上編輯金額 (不需要點進去)
    list_editable = ('amount', 'category')