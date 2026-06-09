#!/usr/bin/env python
"""Django 管理指令入口。

此檔案是整個 Django 專案在命令列上的進入點，常見用法例如：
- python manage.py runserver
- python manage.py makemigrations
- python manage.py migrate

教學重點：
1. 先設定 DJANGO_SETTINGS_MODULE，Django 才知道要讀哪個 settings。
2. 再呼叫 execute_from_command_line，讓 Django 解析並執行命令。
"""
import os
import sys


def main():
    """執行 Django 管理命令。"""
    # 指定預設設定檔，若外部環境已設定同名變數，setdefault 不會覆蓋它。
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'll_project.settings')
    try:
        # 真正負責解析命令列參數（sys.argv）的 Django 函式。
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        # 這段錯誤訊息可幫助初學者快速定位常見問題：
        # 例如沒有安裝 Django、虛擬環境未啟用、PYTHONPATH 設定錯誤等。
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # 將目前指令列參數交給 Django 執行。
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
