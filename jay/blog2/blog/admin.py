from django.contrib import admin
from .models import Blog, Tag, Category, Comment, Post
# Register your models here.

admin.site.register(Blog)
admin.site.register(Tag)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Post)
