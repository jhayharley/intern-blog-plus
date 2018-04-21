from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views import View

from .models import Blog, Post

# Create your views here.

class BlogView(View):
  def get(self, request, pk, *args, **kwargs):
    detail = Detail.objects.get(pk=pk)
    post_list = detail.post_set.all()
    paginator = Paginator(post_list, 5)
    page = request.GET.get('page')
    try:
      post = paginator.page(page)
    except PageNotAnInteger:
      post = paginator.page(1)
    except EmptyPage:
      post = paginator.page(paginator.num_pages)

    context = {
            'detail': detail,
            'post': post,
      }
    return render(request, "blog/detail.html", context)

class PostView(View):
  def get(self, request, post_id, *args, **kwargs):
      post = Post.objects.filter(id=post_id).order_by('-date_created')
      context = {
          'object_list': post,
      }
      return render(request, "blog/post_list.html", context)
