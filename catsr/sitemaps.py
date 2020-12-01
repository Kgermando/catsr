from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from bulletins.models import Bulletin
from evenement.models import Evenenement
from formations.models import Formation

class BulletinSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Bulletin.objects.all()

class EvenenementSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Evenenement.objects.all()

class FormationSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return Formation.objects.all()


class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = 'daily'

    def items(self):
        return ['app:home', 'app:about', 'app:contact', 'app:historique']

    def location(self, item):
        return reverse(item)
