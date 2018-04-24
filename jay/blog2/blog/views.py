from django.shortcuts import render
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import View
from .models import Blog, Post
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)

# Create your views here.class PostView(View):

class PostView(LoginRequiredMixin, View):
  def get(self, request,*args, **kwargs):
      post = Post.objects.all().order_by('-date_created')
      context = {
          'object_list': post,
      }
      return render(request, "blog/post_list.html", context)


class PostDetailView(View):
  def get(self, request, title, *args, **kwargs):
      post = Post.objects.filter(title=title).order_by('-date_created')
      context = {
          'object_list': post,
      }
      return render(request, "blog/post_detail.html", context)
