from django.contrib.sitemaps import Sitemap
from django.core.urlresolvers import reverse


class StaticSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 1.0

    def items(self):
        return ['home', 'profile', 'portfolio', 'blog_index', 'contact']

    def location(self, obj):
        return reverse(obj)
