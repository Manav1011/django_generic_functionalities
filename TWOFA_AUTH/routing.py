from django.urls import re_path
from .consumers import AuthConsumer

websocket_urlpatterns = [
    re_path(r"auth/(?P<secret_key>.+)/$", AuthConsumer.as_asgi()),
]