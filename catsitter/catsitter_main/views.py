from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator


from .forms import PostForm
from .models import Questionnaire, User


def get_page_paginator(request, posts):
    page_namber = request.GET.get('page')
    paginator = Paginator(posts, settings.POSTS_NUM)
    page_obj = paginator.get_page(page_namber)
    return page_obj

# Главная страница
def index(request):
    questionnaires = Questionnaire.objects.select_related('author')
    page_obj = get_page_paginator(request, questionnaires)
    context = {
        'questionnaires': questionnaires,
        'page_obj': page_obj,
    }
    return render(request, 'catsitter_main/index.html', context)

#«Добавлены urls и view-функции»
# Страница со списком мороженого
def catsitter_list(request):
    template = 'catsitter_main/catsitter_list.html'
    return render(request, template)



# Страница с информацией об одном сорте мороженого;
# view-функция принимает параметр pk из path()

def catsitter_detail(request, post_id):
    post = get_object_or_404(Questionnaire, pk=post_id)
    posts_count = Questionnaire.objects.filter(author=post.author).count()
    author = User.objects.get(username=post.author)
    # Здесь код запроса к модели и создание словаря контекста
    context = {
        'post': post,
        'author': author,
        'posts_count': posts_count,
    }
    return render(request, 'catsitter_main/catsitter_detail.html', context)

def profile(request, username):
    author = get_object_or_404(User, username=username)
    posts = Questionnaire.objects.filter(author=author)
    page_obj = get_page_paginator(request, posts)
    count_post = posts.count
    # Здесь код запроса к модели и создание словаря контекста
    context = {
        'author': author,
        'posts': posts,
        'page_obj': page_obj,
        'count_post': count_post,
    }
    return render(request, 'catsitter_main/profile.html', context)

@login_required
def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('catsitter_main:profile', request.user.username)
    return render(request, 'catsitter_main/post_create.html', {'form': form})
        

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Questionnaire, pk=post_id)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        post = form.save()
        post.save()
        return redirect('catsitter_main:catsitter_detail', post_id=post_id)

    # Здесь код запроса к модели и создание словаря контекста
    context = {
        'post': post,
        'form': form,
        'is_edit': True,

        }
    return render(request, 'catsitter_main/post_create.html', context)
