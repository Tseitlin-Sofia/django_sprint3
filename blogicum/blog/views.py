from datetime import datetime
from django.shortcuts import get_object_or_404, render

from blog.models import Post, Category


def post_list():
    post_list = Post.objects.select_related(
        'category',
        'location',
        'author'
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.now()
    )
    return post_list


def index(request):
    template = 'blog/index.html'
    context = {'post_list': post_list()[:5]}
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        post_list(), id=post_id
    )
    context = {'post': post}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    context = {
        'category': category,
        'post_list': post_list().filter(category=category)
    }
    return render(request, template, context)
