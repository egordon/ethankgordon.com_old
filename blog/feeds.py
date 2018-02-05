from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import Article
import re
import markdown

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

class LatestEntriesFeed(Feed):
    title = "Ethan's Blog"
    link = "/blog/"
    description = "Updates on new blog articles."

    def items(self):
        return Article.objects.order_by('-updated')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        html = markdown.markdown(item.text, safe_mode='escape')
        clean = cleanhtml(html)
        return re.match(r'(?:[^.:;]+[.:;]){2}', clean).group()

    def item_link(self, item):
        return reverse('article', args=[item.slug])