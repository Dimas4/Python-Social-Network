from django.shortcuts import render, redirect
from .models import Files, Files_sv
from django.views.generic import TemplateView
from .form import UploadForm
from django.contrib.auth.models import User


def home(request):
    musi = Files_sv.objects.get(current_user=request.user)
    own_music = musi.users.all()
    # music = Files_sv.objects.filter(current_user=request.user)
    # music = Files_sv.objects.all()

    music = Files.objects.all().order_by('-data_time')
    args = {
        'musics': music,
        'own_musics': own_music

    }
    return render(request, "home/homefiles.html", args)

def mymusic(request):
    musi = Files_sv.objects.get(current_user=request.user)
    music = musi.users.all()
    # music = Files_sv.objects.filter(current_user=request.user)
    # music = Files_sv.objects.all()
    print(music)
    args = {
        'musics': music
    }
    return render(request, "home/homemy.html", args)

class Upload(TemplateView):
    template_name = 'home/upload.html'

    def get(self, request):
        form = UploadForm()
        args = {
            'form': form
        }
        return render(request, self.template_name, args)

    def post(self, request):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()

            return redirect('music:home')

        return redirect('music:home')

def change_files(request, operation, pk):
    friend = Files.objects.get(pk=pk)
    if operation == 'add':
        Files_sv.add_files(request.user, friend)
    elif operation == 'remove':
        Files_sv.remove_files(request.user, friend)
    return redirect('music:home')