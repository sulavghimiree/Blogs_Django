from django.shortcuts import render, redirect, get_list_or_404
from .models import Blog

# Create your views here.

def home(request):
    blogs = Blog.objects.all().order_by('-created')[:5]
    return render(request, 'blog_app/home.html', {'blogs':blogs})

def login_user(request):
    return render(request, 'blog_app/login_page.html')
