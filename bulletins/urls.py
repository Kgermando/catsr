
from django.urls import path

from bulletins.views import bulletin_view, bulletin_detail

app_name = 'bulletin'
urlpatterns = [
    path('', bulletin_view, name='bulletin'),
    path('bulletin/<slug:slug>/', bulletin_detail, name='bulletin_detail'),
    path('bulletin/<int:id>/', bulletin_detail, name='bulletin_detail_id')
]
