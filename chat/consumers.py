from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
import json
from django.contrib.auth.models import User
from .models import Message
import datetime
# from .forms import MessageForm

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        if '-' in self.scope['url_route']['kwargs']['room_name']:
            fpk, lpk = self.scope['url_route']['kwargs']['room_name'].split('-')
            if fpk > lpk:
                fpk, lpk = lpk, fpk
            self.room_name = fpk+'-'+lpk
        else:
            self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        pk = text_data_json['pk']
        Message.objects.create(
            text=message,
            user=User.objects.get(pk=pk),
            room=self.room_name,
        )


        # Message.objects.create(text=message, room=self.room_name)




        # new.text = message
        # new.save(self)

        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'pk': pk
            }
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event['message']
        pk = event['pk']
        msg_date = datetime.datetime.now()
        msg_date = str(msg_date)


        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'message': message,
            'msg_date': msg_date,
            'pk': pk,
        }))