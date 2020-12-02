from django.urls import path

from evenement.views import event_view, event_detail

app_name = 'event'
urlpatterns = [
    path('', event_view, name='event'),
    path('event_detail/<slug:slug>/', event_detail, name='event_detail'),
    path('event_detail/<int:id>/', event_detail, name='event_detail_id'),
]
