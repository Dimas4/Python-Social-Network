from django.shortcuts import render
from home.models import Post
from home.forms import HomeForm
from django.core.urlresolvers import resolve
from chat.models import Message
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.models import User

def room(request, room_name):
    if '-' in room_name:
        fpk, lpk = room_name.split('-')
        if fpk > lpk:
            fpk, lpk = lpk, fpk
        room_name = fpk + '-' + lpk
    fpk, lpk = room_name.split('-')
    interlocutor = User.objects.get(pk=fpk)
    messages = Message.objects.filter(room=room_name)
    args = {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'messages': messages,
        'interlocutor': interlocutor

    }
    return render(request, 'chat/room.html', args)


def home(request, pk):
    messages = Post.objects.filter(user_pk__in=[request.user.id, pk], user_send__in=[request.user.id, pk]).order_by('-created')
    form = HomeForm(request.POST)

    pr_k = str(pk)

    args = {
        'messages_moi': messages,
        'form': form,
        'pr_k': pr_k
    }

    return render(request, 'mes/s.html', args)

