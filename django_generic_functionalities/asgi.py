"""
ASGI config for django_generic_functionalities project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_generic_functionalities.settings')

django_asgi_app = get_asgi_application()
from TWOFA_AUTH.routing import websocket_urlpatterns
import TWOFA_AUTH.routing

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": URLRouter(websocket_urlpatterns)    
})
