from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """使用者正在學習的主題。

    一個使用者可以建立多個 Topic；每個 Topic 歸屬於一位 owner。
    """
    # 主題名稱，例如：Python、Django、SQL。
    text = models.CharField(max_length=200)
    # 建立時間，auto_now_add=True 代表只在第一次建立時寫入。
    date_added = models.DateTimeField(auto_now_add=True)
    # 外鍵：Topic 屬於哪位使用者。
    # on_delete=models.CASCADE 表示當使用者被刪除時，相關 Topic 一併刪除。
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """後台、Shell 顯示物件時的可讀字串。"""
        return self.text


class Entry(models.Model):
    """某主題下的一筆學習筆記。"""
    # 每則 Entry 都必須屬於一個 Topic。
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # 筆記正文。
    text = models.TextField()
    # 筆記建立時間。
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Django 在 admin / 部分訊息會用到複數名稱。
        verbose_name_plural = 'entries'

    def __str__(self):
        """回傳摘要字串，避免列表畫面過長。"""
        return f"{self.text[:50]}..."