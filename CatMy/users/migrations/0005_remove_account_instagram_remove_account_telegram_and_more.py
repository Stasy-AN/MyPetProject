# Generated by Django 4.2.7 on 2024-01-09 04:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_favoritearticle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='instagram',
        ),
        migrations.RemoveField(
            model_name='account',
            name='telegram',
        ),
        migrations.RemoveField(
            model_name='account',
            name='vk',
        ),
    ]
