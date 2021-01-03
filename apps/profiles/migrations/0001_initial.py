# Generated by Django 3.0.3 on 2020-08-08 10:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ThinkUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='think_title')),
                ('text', models.CharField(max_length=360, verbose_name='think_text')),
                ('pud_date', models.DateTimeField(verbose_name='think_pud_date')),
                ('connect', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='progress_name')),
                ('description', models.CharField(max_length=360, verbose_name='progress_description')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_user', models.IntegerField(verbose_name='id_user')),
                ('donate', models.IntegerField(verbose_name='donate_user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FavoritePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_post', models.IntegerField(verbose_name='id_post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExtraUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.IntegerField(verbose_name='Phone')),
                ('icon_id', models.IntegerField(blank=True, choices=[(0, 'Icon0'), (1, 'Icon1'), (2, 'Icon2'), (3, 'Icon3'), (4, 'Icon4'), (5, 'Icon5'), (6, 'Icon6'), (7, 'Icon7'), (8, 'Icon8'), (9, 'Icon9'), (10, 'Icon10')], null=True, verbose_name='Icon ID')),
                ('icon_color_1', models.CharField(blank=True, max_length=14, null=True, verbose_name='Color 1')),
                ('icon_color_2', models.CharField(blank=True, max_length=14, null=True, verbose_name='Color 2')),
                ('icon_color_3', models.CharField(blank=True, max_length=14, null=True, verbose_name='Color 3')),
                ('karma', models.IntegerField(default=0, verbose_name='Karma')),
                ('money', models.IntegerField(default=0, verbose_name='Money')),
                ('filter', models.TextField(blank=True, null=True, verbose_name='filter')),
                ('progress', models.ManyToManyField(to='profiles.Progress')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ArchiveUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='archive_title')),
                ('type', models.IntegerField(choices=[(0, 'Folder'), (1, 'Post')], verbose_name='arhive_type')),
                ('parent', models.IntegerField(verbose_name='parent folder id')),
                ('child', models.TextField(blank=True, null=True, verbose_name='child folder id')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]