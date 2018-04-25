from django.conf import settings
from django.urls import reverse
from django.db import models
User = settings.AUTH_USER_MODEL

# Create your models here.

class Blog(models.Model):
    heading          = models.CharField(max_length=120)
    sub_heading      = models.CharField(max_length=120)

    def __str__(self):
        return '{}'.format(self.heading)

class Tag(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    title            = models.CharField(max_length=120)
    date_created     = models.DateTimeField(auto_now_add=True)
    date_modified    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

class Category(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    title            = models.CharField(max_length=120)
    date_created     = models.DateTimeField(auto_now_add=True)
    date_modified    = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.title)

class Comment(models.Model):
    post             = models.ForeignKey('Post', on_delete=models.CASCADE)
    date_created     = models.DateTimeField(auto_now_add=True)
    author           = models.CharField(max_length=200)
    text             = models.TextField()


    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

STATUS_CHOICES = (
    ('published', 'Published'),
    ('draft', 'Draft'),
    ('hidden', 'Hidden')
)

class Post(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    title            = models.CharField(max_length=120)
    subtitle         = models.CharField(max_length=120)
    banner_photo     = models.ImageField(upload_to = 'static/media')
    blog             = models.ForeignKey(Blog, on_delete=models.CASCADE)
    date_created     = models.DateTimeField(auto_now_add=True)
    date_modified    = models.DateTimeField(auto_now_add=True)
    tags             = models.ManyToManyField("Tag", related_name="tags")
    category         = models.ForeignKey('Category', on_delete=models.CASCADE,)
    body             = models.TextField()
    status           = models.CharField(max_length=9, choices=STATUS_CHOICES, blank=True, default=True)

    def __str__(self):
        return '{}'.format(self.user)