# Generated by Django 3.1.2 on 2020-12-01 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evenenement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre_evenement', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, help_text='Laissez ce champ vide', unique=True)),
                ('img_evenement', models.ImageField(upload_to='event_img/')),
                ('content_evenement', models.TextField()),
                ('editeur', models.CharField(max_length=200)),
                ('created', models.DateTimeField()),
            ],
        ),
    ]
