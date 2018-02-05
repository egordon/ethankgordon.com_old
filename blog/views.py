from django.shortcuts import get_object_or_404, render
from .models import Category, Article
from django.core.cache import cache

MAX_ARTICLES = 5


def index(request):
    current = 'blog'

    # Get most recent article
    recentArticle = Article.objects.latest('created')

    # Map each category to five most recent articles
    categories = Category.objects.all()
    categoryMap = dict()
    for c in categories:
        categoryMap[c] = Article.objects.filter(category__id=c.id).order_by('-updated', 'title')[:MAX_ARTICLES]
    return render(request, 'blog/index.html', locals())


def category(request, category_id):
    current = 'blog'
    category = get_object_or_404(Category, slug=category_id)
    template = 'blog/category.html'

    # Get all articles in category
    articles = Article.objects.filter(category__id=category.id).order_by('-updated', 'title')
    return render(request, template, locals())


def article(request, article_id):
    current = 'blog'
    article = get_object_or_404(Article, slug=article_id)
    category = article.category
    template = 'blog/article.html'
    return render(request, template, locals())
