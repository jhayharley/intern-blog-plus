from django.urls import path

from . import views

from .views import PostView, BlogView

app_name = 'blog'

urlpatterns = [
    path('<int:pk>/', BlogView.as_view(), name='detail'),
    path('post/<int:post_id>/', PostView.as_view(), name='post-list'),
]