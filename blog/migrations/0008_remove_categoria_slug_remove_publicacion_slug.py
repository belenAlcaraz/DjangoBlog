# Generated by Django 4.2.7 on 2023-12-09 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rename_avatar_publicacion_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='publicacion',
            name='slug',
        ),
    ]
