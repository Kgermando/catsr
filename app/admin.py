from django.contrib import admin

from app.models import Home, ContactForm, Team, Doc

admin.site.site_header = 'CATSR ADMIN'
admin.site.site_title = "Interface d'administration de l'Accueil"

# Register your models here.
class HomeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'home_title',
        'created'
    )

    list_filter = (
        'home_title',
        'created'
    )

    search_fields = ['home_title',  'created']
admin.site.register(Home, HomeAdmin)


class ContactFormAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'objet_name',
        'email_id',
        'phone_num',
        'created'
    )

    list_filter = (
        'first_name',
        'objet_name',
        'created'
    )

    search_fields = ['first_name', 'objet_name', 'created',]

admin.site.register(ContactForm, ContactFormAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = (
        'prenom_nom',
        'grade',
        'created'
    )

    list_filter = (
        'prenom_nom',
        'grade',
        'created'
    )

    search_fields = ['prenom_nom', 'grade', 'created',]

admin.site.register(Team, TeamAdmin)


class DocAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'objet',
        'document',
        'created'
    )

    list_filter = (
        'titre',
        'objet',
        'created'
    )

    search_fields = ['titre', 'objet', 'created', ]


admin.site.register(Doc, DocAdmin)
