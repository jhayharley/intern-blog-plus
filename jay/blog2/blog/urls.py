from django.urls import path
from . import views
from .views import PostView, PostDetailView

app_name = 'blog'

urlpatterns = [
    path('', PostView.as_view(), name='post'),
    path('<title>', PostDetailView.as_view(), name='post_detail'),
]