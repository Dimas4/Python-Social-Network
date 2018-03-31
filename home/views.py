from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.utils.safestring import mark_safe
import json

from home.forms import HomeForm, HomeForm2
from home.models import Post, Friend, GlMsg

from chat.models import Message


class users(TemplateView):
    template_name = 'home/home_user.html'

    def get(self, request):
        users = User.objects.exclude(id=request.user.id)
        try:
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
            args = {
                'users': users, 'friends': friends
            }
            return render(request, self.template_name, args)
        except:
            args = {
                'users': users
            }
            return render(request, self.template_name, args)

class friend(TemplateView):
    template_name = 'home/home_friend.html'

    def get(self, request):
        users = User.objects.exclude(id=request.user.id)
        try:
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()
            args = {
                'friends': friends
            }
            return render(request, self.template_name, args)
        except:
            args = {
                'users': 'У вас нет друзей'
            }
            return render(request, self.template_name, args)

class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        messagess = Message.objects.filter(room='global')

        form = HomeForm2()
        msg = GlMsg.objects.all().order_by('-created')[:5]
        posts = Post.objects.filter(user_send=request.user.id).order_by('-created')[:5]
        users = User.objects.exclude(id=request.user.id)[:20]

        try:
            friend = Friend.objects.get(current_user=request.user)
            friends = friend.users.all()[:10]
            args = {
                'form': form, 'posts': posts, 'users': users, 'friends': friends, 'msg': msg, 'room_name_json': mark_safe(json.dumps('global')),
            'messagess': messagess,
            }
            return render(request, self.template_name, args)
        except:
            args = {
                'form': form, 'posts': posts, 'users': users, 'msg': msg, 'room_name_json': mark_safe(json.dumps('global')),
            'messagess': messagess,
            }
            return render(request, self.template_name, args)


    def post(self, request):
        form = HomeForm2(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()


            return redirect('home:home')

        return redirect('home:home')

def allmessage_global(request):
    msg = GlMsg.objects.all().order_by('-created')
    form = HomeForm2(request.POST)
    if request.POST:
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()

    args = {
        'msg': msg,
        'form': form
    }
    return render(request, 'home/home_msg_global.html', args)

def allmessage(request):
    posts = Post.objects.filter(user_send=request.user.id).order_by('-created')
    args = {
        'posts': posts
    }
    return render(request, 'home/home_msg.html', args)


def change_friends(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home:home')

def change_friends_user(request, operation, pk):
    friend = User.objects.get(pk=pk)
    if operation == 'add':
        Friend.make_friend(request.user, friend)
    elif operation == 'remove':
        Friend.lose_friend(request.user, friend)
    return redirect('home:users')


def send_msg(request, pk):
    form = HomeForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.user_pk = request.user.pk
        post.user_send = pk
        post.save()
        return redirect('home:home')
    return redirect('home:home')

def send_msgs(request, pk):
    form = HomeForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.user = request.user
        post.user_pk = request.user.pk
        post.user_send = pk
        post.save()
        return redirect('/messages/'+str(pk))
    return redirect('/messages/'+str(pk))

    # return HttpResponseRedirect('/account/profile/'+ str(pk) )