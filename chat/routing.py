# chat/routing.py

from django.conf.urls import url

from . import consumers

websocket_urlpatterns = [
    url(r'^ws/chat/(?P<room_name>[^/]+)/$', cosnumers.ChatConsumer),
]

'''This file is analogous to urls.py of django.
It has the routing configuration. THis routes different requests to appropriate consumers. '''