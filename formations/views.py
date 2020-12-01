from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from formations.models import Formation
# Create your views here.

def formations_view(request):
    """
    docstring
    """
    formation = Formation.objects.all().order_by('-created')
    paginator = Paginator(formation, 9)
    page = request.GET.get('page')
    try:
        formation_list = paginator.page(page)
    except PageNotAnInteger:
        formation_list = paginator.page(1)
    except EmptyPage:
        formation_list = paginator.page(paginator.num_pages)
    context = {
        'formation_list': formation_list,
    }
    template_name = 'pages/formations/formations.html'
    return render(request, template_name, context)

def formations_detail(request, slug):
    """
    docstring
    """
    formation = get_object_or_404(Formation, slug=slug)
    formation_list = Formation.objects.all().order_by('-created')[:5]
    context = {
        'formation': formation,
        'formation_list': formation_list
    }
    template_name = 'pages/formations/formations-detail.html'
    return  render(request, template_name, context)

