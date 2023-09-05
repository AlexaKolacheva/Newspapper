from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, CustomUserChangeForm

from django.contrib.auth.decorators import login_required
from .models import CustomUser
from main.models import Article


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile', user.id)
        else:
            error_message = "Неправильное имя пользователя или пароль"
            return render(request, 'main/login.html', {'error_message': error_message})
    return render(request, 'main/login.html')
"""
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'main/login.html')
    
"""


def logout_view(request):
    logout(request)
    return redirect('/')


def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request,user)
            return redirect('/')
    else:
        form = CustomUserCreationForm()
    return render(request, 'main/register.html', {'form': form})

def profile_view(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    article_list = Article.objects.filter(author__user__id=user.id)
    return render(request, 'main/profile.html', {'user': user, 'article_list':article_list})


@login_required
def edit_profile(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, request.FILES, request.user)
        if form.is_valid():
            form.save()
            return redirect('main/profile.html',
                            pk=request.user.pk)
    else:
        form = CustomUserChangeForm(instance=user)
    context = {
        'form': form
        }

    return render(request, 'main/edit_profile.html', context)
