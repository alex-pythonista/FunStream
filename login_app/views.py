# framework imports

from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# project imports

from .forms import SignUpForm, LoginForm
from .models import Profile
# Create your views here.

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = Profile(user=user)
            user_profile.save()
            return HttpResponseRedirect(reverse('login_app:login'))

    return render(request, 'login_app/sign_up.html', {'form': form})

def login_page(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('stream_app:home'))

    return render(request, 'login_app/login.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('stream_app:home'))

@login_required
def profile(request):
    return render(request, 'login_app/profile.html', {})
