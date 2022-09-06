from django.shortcuts import render, get_object_or_404
from .models import Post, Group
from django.core.paginator import Paginator

MESSAGE_N = 10


def index(request):
    template = 'posts/index.html'
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, MESSAGE_N)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:MESSAGE_N]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
