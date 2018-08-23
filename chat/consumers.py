#chat/consumers.py
'''
This file is somewhat equivalent to views.py of Django.
What happens is that when Channels has a Websocket connection,
the root routing config is lookedup for a consumer, and then calls various functions
on the consumer to handle evets from the connection. '''
from channels.generic.websocket import WebsocketConsumer
import json

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))