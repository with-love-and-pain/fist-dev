# Generated by Django 4.0.3 on 2022-11-04 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fac_news', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newscommentary',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор'),
        ),
        migrations.AddField(
            model_name='newscommentary',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fac_news.news', verbose_name='Новость'),
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='tags.tags', verbose_name='Теги'),
        ),
    ]