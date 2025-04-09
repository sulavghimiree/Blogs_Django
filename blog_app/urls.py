from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_user, name='login-page'),
    path('signup/', views.signup_user, name='signup-page'),
    path('logout/', views.logout_user, name="logout-user"),
    path('create-blog/', views.create_blog, name='create-blog'),
    path('blog/<int:pk>/', views.blog_detail, name="blog-detail"),
    path('blog/delete/<int:pk>', views.delete_blog, name="delete-blog"),
    path('blog/all', views.blog_list, name='blog-list')
]