# Generated by Django 3.1.1 on 2021-01-03 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0025_auto_20201227_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrauser',
            name='icon_id',
            field=models.IntegerField(choices=[(2, 'Icon2'), (3, 'Icon3'), (4, 'Icon4'), (5, 'Icon5'), (6, 'Icon6'), (7, 'Icon7'), (8, 'Icon8'), (9, 'Icon9'), (10, 'Icon10'), (11, 'Icon11')], default=8, verbose_name='Icon ID'),
        ),
    ]