"""WSGI 進入點。

WSGI 是傳統同步部署介面，常見於 Gunicorn + Nginx 架構。
在教學專案中，了解它與 ASGI 都是「伺服器呼叫 Django 的入口」即可。
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'll_project.settings')

# 提供給 WSGI 伺服器呼叫的應用物件。
application = get_wsgi_application()
