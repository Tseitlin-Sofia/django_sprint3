from django.shortcuts import get_object_or_404, render
from blog.models import Post
from datetime import datetime


def index(request):
    template = 'blog/index.html'
    post_list = Post.objects.values(
        'location_base',
        'title',
        'author',
        'category_base').filter(
        pub_date__lte=datetime.now(),
        category_base=True,
        category_base__is_published=True)
    context = {'post_list': post_list}
    print(post_list.query)
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    context = {'post': None}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category': category_slug}
    return render(request, template, context)
