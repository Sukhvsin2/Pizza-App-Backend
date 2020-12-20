"""
ASGI config for pizzaBackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddleware
from channels.routing import URLRouter, ProtocolTypeRouter

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzaBackend.settings')

application = get_asgi_application()

ws_patter = []

application = ProtocolTypeRouter({
    "websocket": AuthMiddleware(URLRouter(ws_patter))
})