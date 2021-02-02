from django.contrib import admin

admin.site.site_header = 'CATSR ADMIN'
admin.site.site_title = "Interface d'administration de l'Accueil"

from bulletins.models import Bulletin

# from tinymce.widgets import TinyMCE
# from tinymce import HTMLField

# Register your models here.
class BulletinAdmin(admin.ModelAdmin):

    # formfield_overrides = {
    #     models.TextField: {'widget': TinyMCE()}
    # }

    # content_bulletin

    list_display = (
        'id',
        'titre_bulletin',
        'slug',
        # 'numero_bulletin',
        'created'
    )

    list_filter = (
        'titre_bulletin',
        'created'
    )

    search_fields = ['titre_bulletin', 'created',]

    list_per_page = 50


admin.site.register(Bulletin, BulletinAdmin)
