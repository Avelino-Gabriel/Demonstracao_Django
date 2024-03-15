"""
ASGI config for clinica project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter, ProtocolTypeRouter
from django.core.asgi import get_asgi_application
import pacientes.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'clinica.settings')
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AuthMiddlewareStack(
        URLRouter(
            pacientes.routing.websocket_urlpatterns
        )
    ),
})


