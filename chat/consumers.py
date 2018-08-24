#chat/consumers.py
'''
This file is somewhat equivalent to views.py of Django.
What happens is that when Channels has a Websocket connection,
the root routing config is lookedup for a consumer, and then calls various functions
on the consumer to handle evets from the connection. '''
from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        #Join room group

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        #Leave from the chat room
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )
        
    #Interesting stuff:
    # Receiving messages from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        #Send message to the group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    #Receive message from room group
    def chat_message(self, event):
        message = event['message']

        #Send messages to WebSocket
        self.send(text_data=json.dumps({
            'message' : message
        }))