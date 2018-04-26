from django.shortcuts import render
from django.views import View
from django.shortcuts import render, Http404, get_object_or_404, redirect
from .forms import CommentForm
from .models import Blog, Post,Comment
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
        post = get_object_or_404(Post, title=title, status='published')
        comment = post.comment_set.all()
        context = {'post':post,'comment': comment,}

        return render(request, "blog/post_detail.html", context)

def comment(request):
  if request.method == 'POST':
      form = CommentForm(request.POST)
      if form.is_valid():
          comment = form.save(commit=False)
          comment.save()
          return redirect('/posts')
  else:
      form = CommentForm()
  context = {
      'form': form,
  }
  return render(request, 'blog/comment.html', context)
