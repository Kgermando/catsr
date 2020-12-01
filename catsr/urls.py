"""catsr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path


from django.contrib.sitemaps.views import sitemap
from .sitemaps import BulletinSitemap, EvenenementSitemap, FormationSitemap, StaticViewSitemap


sitemaps = {
    'bulletins-view' : BulletinSitemap,
    'evenement-view' : EvenenementSitemap,
    'formations-view' : FormationSitemap,
    'static': StaticViewSitemap,
    }


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('', include('app.urls')),
    path('bulletins/', include('bulletins.urls')),
    path('formations/', include('formations.urls')),
    path('evenement/', include('evenement.urls')),
    path('@catsr/', admin.site.urls),
]

handler400 = 'handlers.views.handler400'
handler403 = 'handlers.views.handler403'
handler404 = 'handlers.views.handler404'
handler500 = 'handlers.views.handler500'

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
