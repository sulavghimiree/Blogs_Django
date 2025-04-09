from django.shortcuts import render, redirect, get_list_or_404
from .models import Blog
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm

# Create your views here.

def home(request):
    blogs = Blog.objects.filter(is_published=True).order_by('-created')[:5]
    return render(request, 'blog_app/home.html', {'blogs':blogs})

def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid Username or Password')
    return render(request, 'blog_app/login_page.html')

def logout_user(request):
    logout(request)
    return redirect('home')

def signup_user(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('login-page')
    else:
        form = UserCreationForm()
    return render(request, 'blog_app/signup_page.html', {'form':form})
