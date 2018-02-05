from django.db import models
import xml.etree.cElementTree as et
from django.contrib.auth.models import User

# Working with SVGs

def is_svg(f):
    tag = None
    try:
        for event, el in et.iterparse(f, ('start',)):
            tag = el.tag
            break
    except et.ParseError:
        pass
    return tag == '{http://www.w3.org/2000/svg}svg'

def validate_svg(file):
    if not is_svg(file.file):
        raise ValidationError("File not svg")

# Create your models here.

class Category(models.Model):
    '''
    Article categories, with description and image
    '''
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='categories', validators=[validate_svg], blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    slug = models.SlugField(
        verbose_name = 'Slug', 
        help_text = 'Uri identifier for this category.', 
        unique = True,
        max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

class Figure(models.Model):
    '''
    Image to add to article.
    '''
    image = models.ImageField(upload_to='figures', blank=False, null=False)
    caption = models.TextField(blank=True)

    def __str__(self):
        return self.image.url

class Article(models.Model):
    title = models.CharField(
        max_length=100, 
        blank=False, 
        null=False);
    slug = models.SlugField(
        verbose_name = 'Slug', 
        help_text = 'Uri identifier for this Article.', 
        unique = True,
        max_length=100)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    author = models.ForeignKey(User)
    text = models.TextField(blank=False, null=False)
    category = models.ForeignKey(Category)
    majorUpdates = models.BooleanField(default=False, null=False)
    figures = models.ManyToManyField(
        Figure,
        through         = 'ArticleFigures',
        related_name    = 'figures',
        verbose_name    = 'Figures',
        help_text       = 'Figures in this article.'
    )

    def __str__(self):
        return self.title

class ArticleFigures(models.Model):
    article = models.ForeignKey(
        Article,
        verbose_name    = 'Article'
    )
    figure = models.ForeignKey(
        Figure,
        verbose_name    = 'Figure',
    )       
    order = models.IntegerField(
        verbose_name    = 'Order',
        help_text       = 'Figure display order.'
    )

    class Meta:
        verbose_name = "Article Figure"
        verbose_name_plural = "Article Figures"
        ordering = ['order',]

    def __str__(self):
        return str(self.figure) + "(Figure " + str(self.order) + " of " + self.article.title + ")"

