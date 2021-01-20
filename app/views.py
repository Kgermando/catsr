from django.shortcuts import render,redirect
from django.contrib import messages # for message
from django.urls import reverse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from app.models import Home, ContactForm, Team, Doc
from bulletins.models import Bulletin
from evenement.models import Evenenement
from formations.models import Formation

# Create your views here.

def home_view(request):
    """
    docstring
    """
    home_list = Home.objects.all().order_by('-created')[:1]
    bulletin_list = Bulletin.objects.all().order_by('-created')[:4]
    evenenement_list = Evenenement.objects.all().order_by('-created')[:4]
    formation_list = Formation.objects.all().order_by('-created')[:4]
    context = {
        'home_list': home_list,
        'bulletin_list': bulletin_list,
        'evenenement_list': evenenement_list,
        'formation_list': formation_list
    }
    template_name = 'pages/app/home.html'
    return render(request, template_name, context)


def contact_view(request):
    if  request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        objet_name = request.POST['objet_name']
        email_id = request.POST['email_id']
        phone_num = request.POST['phone_num']
        message = request.POST['message']
        contact_us = ContactForm(first_name=first_name,last_name=last_name,objet_name=objet_name,email_id=email_id,phone_num=phone_num,message=message)
        contact_us.save()
        # send_mail(first_name, )
        messages.success(request,'! Nous avons réçu votre message')
        return redirect('/contact')

    template_name = 'pages/app/contact.html'
    return render(request, template_name, context=None)

def about_view(request):
    """
    docstring
    """
    team_list = Team.objects.all().order_by('-created')
    context = {
        'team_list': team_list
    }
    template_name = "pages/app/about.html"
    return render(request, template_name, context)

def historique_view(request):
    """
    docstring
    """
    docs = Doc.objects.all()
    context = {
        'docs': docs
    }
    template_name = "pages/app/historique.html"
    return render(request, template_name, context)


def docs_view(request):
    """
    docs juridique
    """
    if request.method == 'POST':
        titre = request.POST['titre']
        objet = request.POST['objet']
        document = request.FILES['document']
        docs = Doc(titre=titre, objet=objet, document=document)
        docs.save()
        messages.success(request, '! Nous avons réçu votre message')
        return redirect('/historique')
    template_name = "pages/app/docs.html"
    return render(request, template_name, context=None)
