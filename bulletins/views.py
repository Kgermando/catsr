from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from bulletins.models import Bulletin
# Create your views here.
def bulletin_view(request):
    """
    docstring
    """
    bulletin = Bulletin.objects.all().order_by('-created')
    paginator = Paginator(bulletin, 9)
    page = request.GET.get('page')
    try:
        bulletin_list = paginator.page(page)
    except PageNotAnInteger:
        bulletin_list = paginator.page(1)
    except EmptyPage:
        bulletin_list = paginator.page(paginator.num_pages)
    context = {
        'bulletin_list': bulletin_list,
    }
    template_name = 'pages/bulletins/bulletins.html'
    return render(request, template_name, context)

def bulletin_detail(request, slug):
    """
    docstring
    """
    bulletin = get_object_or_404(Bulletin, slug=slug)
    bulletin_list = Bulletin.objects.all().order_by('-created')[:5]
    bulletin.nombre_vues = bulletin.nombre_vues+1
    bulletin.save()
    context = {
        'bulletin': bulletin,
        'bulletin_list': bulletin_list
    }
    template_name = 'pages/bulletins/bulletin-detail.html'
    return  render(request, template_name, context)
