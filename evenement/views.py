from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from evenement.models import Evenenement

# Create your views here.
def event_view(request):
    """
    docstring
    """
    event = Evenenement.objects.all().order_by('-created')
    paginator = Paginator(event, 9)
    page = request.GET.get('page')
    try:
        event_list = paginator.page(page)
    except PageNotAnInteger:
        event_list = paginator.page(1)
    except EmptyPage:
        event_list = paginator.page(paginator.num_pages)
    context = {
        'event_list': event_list,
    }
    template_name = 'pages/event/event.html'
    return render(request, template_name, context)

def event_detail(request, slug):
    """
    docstring
    """
    event = get_object_or_404(Evenenement, slug=slug)
    event_list = Evenenement.objects.all().order_by('-created')[:5]
    context = {
        'event': event,
        'event_list': event_list
    }
    template_name = 'pages/event/event_detail.html'
    return render(request, template_name, context)
