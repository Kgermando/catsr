# Generated by Django 3.1.2 on 2020-12-20 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletins', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='enfants_scolarise_filles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bulletin',
            name='total_enfant_scolarise',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
