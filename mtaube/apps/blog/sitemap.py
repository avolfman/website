from django.contrib.sitemaps import Sitemap

from mtaube.apps.blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.5

    def items(self):
        return Post.objects.filter(is_active=True)
