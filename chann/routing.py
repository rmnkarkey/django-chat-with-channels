from django.urls import re_path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'^(?P<category_name_id>[^/]+)/(?P<room_id>[^/]+)/(?P<users_id>[^/]+)$', ChatConsumer),
]