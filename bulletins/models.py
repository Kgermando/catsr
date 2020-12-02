from django.db import models
from django.db.models.signals import pre_save
from catsr.utils import unique_slug_generator

# Create your models here.
class Bulletin(models.Model):
    """
    docstring
    """
    titre_bulletin = models.CharField(max_length=200)
    slug = models.SlugField(blank=True, unique=True, help_text='Laissez ce champ vide')
    img_bulletin = models.ImageField(upload_to='bulletin_img/')
    content_bulletin = models.TextField()
    numero_bulletin = models.IntegerField()
    total_enfant_scolarise = models.IntegerField(blank=True, )
    enfants_scolarise_filles = models.IntegerField(blank=True, )
    enfants_formation_professionnelle = models.IntegerField(blank=True, null=True, help_text='orientés et accompagnés en formation professionnelle ')
    enfants_formation_professionnelle_filles = models.IntegerField(blank=True, null=True, help_text='orientés et accompagnés en formation professionnelle ')
    enfants_jeunes_adultes = models.IntegerField(blank=True, null=True, help_text='enfants, jeunes et adultes contactés lors de la descente sur le terrain ')
    nombre_enfants_identifies = models.IntegerField(blank=True, null=True, help_text='Uniquement les chiffres')
    nombre_contacts = models.IntegerField(blank=True, null=True, help_text='Uniquement les chiffres')
    nombre_entretiens_realises = models.IntegerField(blank=True, null=True, help_text='Uniquement les chiffres')
    nombre_suivi_familial = models.IntegerField(blank=True, null=True, help_text='Uniquement les chiffres')
    nombre_enquetes_realises = models.IntegerField(blank=True, null=True, help_text='Uniquement les chiffres')
    nombre_suivi_scolarise = models.IntegerField(blank=True, null=True, help_text='Uniquement les chiffres')
    nombre_suivi_formations_professionnelles = models.IntegerField(blank=True, null=True, help_text='Uniquement les chiffres')
    nombre_animations_rue = models.IntegerField(blank=True, null=True, help_text='Uniquement les chiffres')
    nombre_reinsertions_familiales = models.IntegerField(blank=True, null=True, help_text='Uniquement les chiffres')
    editeur = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=False)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('bulletin:bulletin_detail_id', args=[str(self.id)])

    def __str__(self):
        return self.titre_bulletin


def tag_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(tag_pre_save_receiver, sender=Bulletin)
