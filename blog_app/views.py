from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Blog
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CustomUserCreationForm, BlogForm
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='login-page')
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('home')
    else:
            form = BlogForm()
    return render(request, 'blog_app/create_blog.html', {'form':form})

def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk, is_published=True)
    return render(request, 'blog_app/blog_detail.html', {"blog":blog})

@login_required(login_url='login-page')
def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)

    if request.method == "POST":
        blog.delete()
        return redirect('home')
    return render(request, 'blog_app/delete_blog.html', {'blog':blog})

def blog_list(request):
    blogs = Blog.objects.filter(is_published=True).order_by('-created')
    return render(request, 'blog_app/blog_list.html', {'blogs':blogs})

def about_view(request):
    return render(request, 'blog_app/about_page.html')

@login_required(login_url='login-page')
def user_profile(request, username):
    if username:
        try:
            profile_user = User.objects.get(username=username)
        except User.DoesNotExist:
            return messages.error(request, 'User not found')
    else:
        profile_user = request.user

    is_own_profile = (profile_user == request.user)
    print(profile_user)

    published = profile_user.blog_set.filter(is_published=True).order_by('-created')
    unpublished = profile_user.blog_set.filter(is_published=False).order_by('-created') if is_own_profile else None

    return render(request, 'blog_app/user_profile.html', {
        'profile_user':profile_user,
        'published_blogs':published,
        'unpublished_blogs':unpublished,
        'is_own_profile': is_own_profile
    })
