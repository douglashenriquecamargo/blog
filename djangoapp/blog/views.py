from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.models import User
from django.http import Http404
from blog.models import Page, Post

PER_PAGE = 9

def index(request):
    posts = Post.objects.get_published()

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'page_title': 'Home - '
    }

    return render(request, 'blog/pages/index.html', context)


def created_by(request, author_pk):
    user = User.objects.filter(pk=author_pk).first
    posts = Post.objects.get_published().filter(created_by__pk=author_pk)

    if user is None:
        raise Http404()

    user_full_name = user.username

    if user.first_name:
        user_ful_name = f'{user.first_name} {user.last_name}'

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': f'{user_full_name} page - '
        }
    )


def category(request, slug):
    posts = Post.objects.get_published().filter(category__slug=slug)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
   
    if len(page_obj) == 0:
        raise Http404()

    return render(
        request,
        'blog/pages/index.html',
        {
            'page_obj': page_obj,
            'page_title': f'{page_obj[0].category.name} - Categoria - '
        }
    )


def tag(request, slug):
    posts = Post.objects.get_published().filter(tags__slug=slug)

    paginator = Paginator(posts, PER_PAGE)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    if len(page_obj) == 0:
        raise Http404()
    
    context = {
        'page_obj': page_obj,
        'page_title': f'{page_obj[0].tags.first().name} - Tag - '
        }
    
    return render(
        request,
        'blog/pages/index.html',
        context
    )


def search(request):
    search_value = request.GET.get('search', '').strip()
    posts = (
        Post.objects.get_published()
            .filter(
                Q(title__icontains=search_value) |
                Q(excerpt__icontains=search_value) |
                Q(content__icontains=search_value)
            )[:PER_PAGE]
    )
    
    context = {
            'page_obj': posts,
            'search_value': search_value,
            'page_title': f'{search_value[:30]} - Search - '
        }
    
    return render(
        request,
        'blog/pages/index.html',
        context
    )

def page(request, slug):
    page_object = (
        Page.objects.get_published()
        .filter(slug=slug)
        .first()
    )

    if page_object is None:
        raise Http404()

    context = {
        'page': page_object,
        'page_title': f'{page_object.title} - Página'
    }

    return render(
        request,
        'blog/pages/page.html',
        context
    )


def post(request, slug):
    post_object = (
        Post.objects.get_published()
        .filter(slug=slug)
        .first()
    )

    if post_object is None:
        raise Http404()

    context = {
        'post': post_object,
        'page_title': f'{post_object[0].title} - Post - '
    }

    return render(
        request,
        'blog/pages/post.html',
        context
    )