from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from .models import Message
from django.contrib.auth.models import User

def room(request, room_name):
    fpk, lpk = room_name.split('-')
    interlocutor = User.objects.get(pk=fpk)
    messages = Message.objects.filter(room=room_name)
    args = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'messages': messages,
        'interlocutor': interlocutor

    }
    return render(request, 'chat/room.html', args)