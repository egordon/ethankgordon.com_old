from django.contrib import admin
from .models import Category, Figure, Article, ArticleFigures

# Register your models here.
class ArticleFiguresInline(admin.TabularInline):
    model = ArticleFigures
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = (ArticleFiguresInline,)

class FigureAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category)
admin.site.register(Figure, FigureAdmin)
admin.site.register(Article, ArticleAdmin)
