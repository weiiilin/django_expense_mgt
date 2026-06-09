from django.apps import AppConfig


class LearningLogsConfig(AppConfig):
    """learning_logs app 設定。"""

    # Django 3.2+ 建議使用 BigAutoField 作為預設主鍵型別。
    default_auto_field = 'django.db.models.BigAutoField'
    # 此 app 在專案中的註冊名稱（需對應 INSTALLED_APPS）。
    name = 'learning_logs'
