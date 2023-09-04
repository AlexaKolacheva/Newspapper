from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Article, Category,Tags, Author
from .forms import ArticleForm, CategoryForm, CommentForm
from django.http import Http404



def index(request):
    articles = Article.objects.all()
    categories = Category.objects.all()
    context = {
        'article_list': articles,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def get_article_by_category(request, category_id):
    articles = Article.objects.filter(category__id=category_id)
    categories = Category.objects.all()
    context = {
        'article_list': articles,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def get_article_by_tag(request, tag_id):
    articles = Article.objects.filter(tags__id=tag_id)
    categories = Category.objects.all()
    context = {
        'article_list': articles,
        'categories': categories
    }
    return render(request, 'main/index.html', context)


def detail_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            if request.user.is_authenticated:
                author = Author.objects.get(user=request.user)
                comment.user = author
                comment.article= article
                comment.save()
                error_message= 'Авторизуйтесь, чтобы добавлять комментарии'
    else:
        form = CommentForm()
        error_message =None
    context = {
        'article': article,
        'form': form,
        'error_message': error_message
    }

    return render(request, 'main/detail_article.html', context)


"""
def detail_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    context = {
        'article': article
    }

    return render(request, 'main/detail_article.html', context)

"""

def create_article(request):

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save()

            new_tags = form.cleaned_data.get('new_tags')
            if new_tags:
                tag_names = [tag.strip() for tag in new_tags.split(',')]
                for tag_name in tag_names:
                    tag, created = Tags.objects.get_or_create(tag_name=tag_name)
                    article.tags.add(tag)

            article.save()
            return redirect('/')
    else:
        form = ArticleForm()

    return render(request, 'main/create_article.html', {'form': form})



def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = CategoryForm()

    context = {
        'form': form,
    }
    return render(request, 'main/add_category.html', context)

def delete_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)

    if request.method == 'POST':
        article.delete()
        return redirect('/')

    context = {
        'article': article
    }
    return render(request, 'main/delete_article.html', context)


def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            article = form.save()

            new_tags = form.cleaned_data.get('new_tags')
            if new_tags:
                tag_names = [tag.strip() for tag in new_tags.split(',')]
                for tag_name in tag_names:
                    tag, created = Tags.objects.get_or_create(tag_name=tag_name)
                    article.tags.add(tag)

            article.save()
            return redirect('/')
    else:
        form = ArticleForm(instance=article)

    context = {
            'article': article,
            'form': form
        }

    return render(request, 'main/edit_article.html', context)

