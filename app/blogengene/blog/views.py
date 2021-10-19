from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import View
from django.core.paginator import Paginator

from .models import *
from .utils import *

# Create your views here.
def posts_list(request):    
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)

    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()

    prev_url = '?page={}'.format(page.previous_page_number()) if page.has_previous() else ''
    next_url = '?page={}'.format(page.next_page_number()) if page.has_next() else ''

    context = {
        'posts':page,
        'is_paginated':is_paginated,
        'prev_url':prev_url,
        'next_url':next_url,
    }

    return render(request, 'blog/index.html', context = context)

class PostDetail(ObjectDetailMixin, View):
    model = Post
    templated = 'blog/post_detail.html'

def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context = {'tags':tags})

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    templated = 'blog/tag_detail.html'