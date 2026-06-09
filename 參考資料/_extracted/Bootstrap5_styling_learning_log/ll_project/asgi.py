"""ASGI 進入點。

ASGI 常見於非同步伺服器（例如 Uvicorn / Daphne），
若未使用 WebSocket 或大量 async 情境，初學期可先把它視為部署入口之一。
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'll_project.settings')

# 提供給 ASGI 伺服器呼叫的應用物件。
application = get_asgi_application()
