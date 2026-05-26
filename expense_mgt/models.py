from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ExpenseRecord(models.Model):
    # 關聯到 User 模型，表示這筆消費記錄屬於哪個使用者
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')

    # 1. 實際消費日期 (讓使用者可以選擇哪一天消費)
    # 預設值設為 timezone.now，確保沒選日期時也會抓今天
    date = models.DateField(default=timezone.now)
    
    # 2. 消費類別
    category = models.CharField(max_length=50)
    
    # 3. 金額
    amount = models.IntegerField()
    
    # 4. 備註
    description = models.CharField(max_length=200, blank=True)
    
    # 5. 系統建立時間 (隱藏欄位，用於記錄這筆資料何時被存入)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # 讓排序依照「消費日期」由新到舊，如果日期相同則看「系統建立時間」
        ordering = ['-date', '-created_at']

    def __str__(self):
        return f"{self.date} | {self.category}: {self.amount}"