# Generated by Django 4.2.7 on 2024-01-05 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_viewcount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('E', 'Экономика'), ('N', 'Новости'), ('J', 'Жилье'), ('R', 'Разное')], max_length=20, verbose_name='Категории'),
        ),
    ]
