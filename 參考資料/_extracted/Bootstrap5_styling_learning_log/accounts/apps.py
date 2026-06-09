from django.apps import AppConfig


class AccountsConfig(AppConfig):
    """accounts app 設定。"""

    # Django 3.2+ 預設主鍵型別。
    default_auto_field = 'django.db.models.BigAutoField'
    # app 名稱，需與 INSTALLED_APPS 設定一致。
    name = 'accounts'
