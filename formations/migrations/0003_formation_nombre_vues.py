# Generated by Django 3.1.2 on 2021-05-26 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formations', '0002_auto_20210202_0743'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='nombre_vues',
            field=models.IntegerField(default=0, verbose_name='Nombre des vues'),
        ),
    ]
