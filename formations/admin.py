from django.contrib import admin

admin.site.site_header = 'CATSR ADMIN'
admin.site.site_title = "Interface d'administration de l'Accueil"

from formations.models import Formation

# Register your models here.
class FormationAdmin(admin.ModelAdmin):
    list_display = (
        'titre_formation',
        'slug',
        'created'
    )

    list_filter = (
        'titre_formation',
        'created'
    )

    search_fields = ['titre_formation',  'created',]

    list_per_page = 50

admin.site.register(Formation, FormationAdmin)
