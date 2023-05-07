# Generated by Django 4.0.3 on 2022-11-04 15:03

from django.db import migrations, models
import django.db.models.deletion
import src.modules.faculty.structure.models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
                ('information', tinymce.models.HTMLField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Кафедра',
                'verbose_name_plural': 'Кафедры',
                'db_table': 'fc_departments',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Название')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
                ('information', tinymce.models.HTMLField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Дисциплина',
                'verbose_name_plural': 'Дисциплины',
                'db_table': 'fc_disciplines',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Techs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='Технология')),
            ],
            options={
                'verbose_name': 'Технология',
                'verbose_name_plural': 'Технологии',
                'db_table': 'fc_tech_skills',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Короткое название')),
                ('full_name', models.CharField(max_length=128, verbose_name='Полное название')),
                ('description', models.CharField(max_length=1024, verbose_name='Описание')),
                ('information', tinymce.models.HTMLField(verbose_name='Текст')),
                ('budget_seats', models.IntegerField(blank=True, default=0, null=True, verbose_name='Бюджетных мест')),
                ('avatar', models.ImageField(default='', upload_to='specialty_image', verbose_name='Изображение направления')),
                ('price', models.IntegerField(default=0, verbose_name='Цена за год')),
                ('years', models.CharField(default='4', max_length=10, verbose_name='Лет обучения')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.department', verbose_name='Кафедра')),
                ('stack_techs', models.ManyToManyField(to='structure.techs')),
                ('tags', models.ManyToManyField(to='tags.tags', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Направление',
                'verbose_name_plural': 'Направления',
                'db_table': 'fc_specialties',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, verbose_name='Строка с подитогом')),
                ('specialty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='structure.specialty', verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'В итоге',
                'verbose_name_plural': 'В итоге',
                'db_table': 'fc_specialty_results',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Lessoner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=32, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=32, null=True, verbose_name='Отчество')),
                ('information', tinymce.models.HTMLField(verbose_name='Текст')),
                ('avatar', models.ImageField(default='no_photo.png', upload_to=src.modules.faculty.structure.models.get_path_for_lessoner_image, verbose_name='Аватар')),
                ('science_rank', models.CharField(default='', max_length=90, verbose_name='Научная степень')),
                ('department', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='structure.department', verbose_name='Кафедра')),
                ('disciplines', models.ManyToManyField(blank=True, to='structure.discipline', verbose_name='Дисциплины')),
                ('tags', models.ManyToManyField(blank=True, to='tags.tags', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Преподаватель',
                'verbose_name_plural': 'Преподаватели',
                'db_table': 'pr_fc_teachers',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Graduate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(default='Не указано', max_length=256, verbose_name='ФИО')),
                ('information', tinymce.models.HTMLField(verbose_name='Текст')),
                ('avatar', models.ImageField(default='no_photo.png', upload_to=src.modules.faculty.structure.models.get_path_for_graduate_image, verbose_name='Аватар')),
                ('rank', models.CharField(blank=True, default=None, max_length=128, null=True, verbose_name='Текущая должность')),
                ('specialty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='structure.specialty', verbose_name='Направление')),
            ],
            options={
                'verbose_name': 'Выпускник',
                'verbose_name_plural': 'Выпускники',
                'db_table': 'pr_fc_graduates',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='discipline',
            name='specialties',
            field=models.ManyToManyField(to='structure.specialty', verbose_name='Направление'),
        ),
        migrations.AddField(
            model_name='discipline',
            name='tags',
            field=models.ManyToManyField(to='tags.tags', verbose_name='Теги'),
        ),
    ]