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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='TEXT')),
                ('parent', models.TextField(blank=True, null=True, verbose_name='parent')),
                ('child', models.TextField(blank=True, null=True, verbose_name='child')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('text', models.TextField(blank=True, null=True, verbose_name='TEXT')),
                ('date', models.DateTimeField(verbose_name='date publish')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='TEXT')),
                ('date', models.DateTimeField(verbose_name='date publish')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('second_images', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('type', models.IntegerField(blank=True, choices=[(0, 'Publish'), (1, 'Hide'), (2, 'Trush'), (3, 'Beta'), (4, 'Alfa')], null=True, verbose_name='type')),
                ('lang', models.IntegerField(blank=True, choices=[(0, 'Publish'), (1, 'Hide'), (2, 'Trush'), (3, 'Beta'), (4, 'Alfa')], null=True, verbose_name='lang')),
                ('black_horse', models.IntegerField(default=0, verbose_name='black_horse')),
                ('virus', models.IntegerField(default=0, verbose_name='virus')),
                ('file_torrent', models.FileField(blank=True, null=True, upload_to='torrent/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='TEXT')),
                ('parent', models.TextField(blank=True, null=True, verbose_name='parent')),
                ('child', models.TextField(blank=True, null=True, verbose_name='child')),
            ],
        ),
        migrations.CreateModel(
            name='StatisticComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0, verbose_name='Value')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0, verbose_name='Value')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Same',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='posts.Tag'),
        ),
        migrations.CreateModel(
            name='ExtraPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Title')),
                ('id_file', models.IntegerField(verbose_name='id_file')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post'),
        ),
        migrations.CreateModel(
            name='ArrayLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField(verbose_name='link')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post')),
            ],
        ),
    ]