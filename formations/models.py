from django.db import models
from django.db.models.signals import pre_save
from catsr.utils import unique_slug_generator_formation

from tinymce import HTMLField

# Create your models here.
class Formation(models.Model):
    """
    docstring
    """
    titre_formation = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    img_formation = models.ImageField(upload_to='formations_img/')
    content_formation = HTMLField('content_formation')
    editeur = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=False)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('formations:formations_detail_id', args=[str(self.id)])

    def __str__(self):
        return self.titre_formation


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator_formation(instance)

pre_save.connect(tag_pre_save_receiver, sender=Formation)
