from django.db import models
from django.db.models.signals import pre_save
from catsr.utils import unique_slug_generator

from tinymce import HTMLField

# Create your models here.
class Bulletin(models.Model):
    """
    docstring
    """
    titre_bulletin = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    img_bulletin = models.ImageField(upload_to='bulletin_img/')
    content_bulletin = HTMLField('content_bulletin')
    editeur = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=False)
    nombre_vues = models.IntegerField(default=0, verbose_name="Nombre des vues")

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('bulletin:bulletin_detail_id', args=[str(self.id)])

    def __str__(self):
        return self.titre_bulletin


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(tag_pre_save_receiver, sender=Bulletin)
