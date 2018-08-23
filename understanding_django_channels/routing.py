#understanding_django_channels/routing.py
from channels.routing import ProtocolTypeRouter
'''
This file is analogous to the root urls.py of a django project.
It specifies root routing config. When a connection is made to 
the Channels development server, the ProtocolTypeRouter examines the
type of connection. If it is a websocket connection (ws:// or wss://), the
connection will be given to AuthMiddlewareStack(this is analogous to the
authentication middleware in django). '''

from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter
import chat.routing 

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket' : AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})