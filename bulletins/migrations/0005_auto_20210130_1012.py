# Generated by Django 3.1.2 on 2021-01-30 09:12

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('bulletins', '0004_auto_20210130_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='content_bulletin',
            field=tinymce.models.HTMLField(verbose_name='Content'),
        ),
    ]
