
from django.urls import path

from formations.views import formations_view, formations_detail

app_name = 'formations'
urlpatterns = [
    path('', formations_view, name='formations'),
    path('formations/<slug:slug>/', formations_detail, name='formations_detail'),
    path('formations/<int:id>/', formations_detail, name='formations_detail_id')
]
