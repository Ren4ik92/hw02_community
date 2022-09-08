from django.shortcuts import render, get_object_or_404
from .models import Post, Group, User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

MESSAGE_N = 10


def index(request):
    template = 'posts/index.html'
    post_list = Post.objects.all().order_by('-pub_date')
    paginator = Paginator(post_list, MESSAGE_N)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'post_list': post_list

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


def profile(request, username):
    author = get_object_or_404(User, username=username)
    user_post_list = Post.objects.filter(author__username=username).order_by('-pub_date')
    paginator = Paginator(user_post_list, MESSAGE_N)
    page_number = request.GET.get('page')
    profile_obj = paginator.get_page(page_number)

    context = {
        'profile_obj': profile_obj,
        'author': author

    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id,):
    post_d = Post.objects.filter(pk=post_id)
    context = {
        'post_d': post_d,
    }
    return render(request, 'posts/post_detail.html', context)
