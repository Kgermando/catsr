from django.db import models

# Create your models here.
class Home(models.Model):
    # home_number = models.IntegerField(default=0, unique=True)
    home_title = models.CharField(max_length=100)
    home_description = models.CharField(max_length=150)
    home_image = models.ImageField(upload_to='home_img/')
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.home_title

class ContactForm(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    objet_name = models.CharField(max_length=255)
    email_id = models.CharField(max_length=101)
    phone_num = models.CharField(max_length=15)
    message = models.TextField() 
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Message de ' + self.first_name + ' ' + self.last_name

class Team(models.Model):
    """
    docstring
    """
    prenom_nom = models.CharField(max_length=255)
    grade = models.CharField(max_length=255)
    img_profile = models.ImageField(upload_to='team_img/')
    created = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.prenom_nom

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('app:about_detail_id', args=[str(self.id)])
    