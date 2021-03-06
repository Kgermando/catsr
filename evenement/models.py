from django.db import models
from django.db.models.signals import pre_save
from catsr.utils import unique_slug_generator_event

from tinymce import HTMLField
 
# Create your models here.
class Evenenement(models.Model):
    titre_evenement = models.CharField(max_length=300)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    img_evenement = models.ImageField(upload_to='event_img/')
    content_evenement = HTMLField('content_evenement')
    editeur = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=False)
    nombre_vues = models.IntegerField(default=0, verbose_name="Nombre des vues")

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('event:event_detail_id', args=[str(self.id)])

    def __str__(self):
        return self.titre_evenement

def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_event(instance)

pre_save.connect(tag_pre_save_receiver, sender=Evenenement)
