
from django.urls import path

from app.views import home_view, contact_view, about_view, historique_view

app_name = 'app'
urlpatterns = [
    path('', home_view, name='home'),
    path('contact', contact_view, name='contact'),
    path('about', about_view, name='about'),
    path('historique', historique_view, name='historique')
]
