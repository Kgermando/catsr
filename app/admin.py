from django.contrib import admin

from app.models import Home, ContactForm, Team

admin.site.site_header = 'CATSR ADMIN'
admin.site.site_title = "Interface d'administration de l'Accueil"

# Register your models here.
admin.site.register(Home)


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