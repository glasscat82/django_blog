from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View

from .models import *
from .utils import *

# Create your views here.
def posts_list(request):    
    posts = Post.objects.all().order_by('-date_pub', 'title')
    return render(request, 'blog/index.html', context = {'posts':posts})

class PostDetail(ObjectDetailMixin, View):
    model = Post
    templated = 'blog/post_detail.html'

def tags_list(request):
    tags = Tag.objects.all().order_by('title')
    return render(request, 'blog/tags_list.html', context = {'tags':tags})

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    templated = 'blog/tag_detail.html'