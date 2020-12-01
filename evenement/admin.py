from django.contrib import admin

from evenement.models import Evenenement
# Register your models here.
class EvenementAdmin(admin.ModelAdmin):
    list_display = (
        'titre_evenement',
        'created'
    )

    list_filter = (
        'titre_evenement',
        'created'
    )

    search_fields = ['titre_evenement', 'created',]

    list_per_page = 50

admin.site.register(Evenenement, EvenementAdmin)
