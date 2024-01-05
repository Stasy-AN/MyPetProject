# Generated by Django 4.2.7 on 2024-01-05 15:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_viewcount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_account_address_account_instagram_account_phone_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('article', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='news.article')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
