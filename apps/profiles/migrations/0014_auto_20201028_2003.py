# Generated by Django 3.1.1 on 2020-10-28 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0013_auto_20201028_2003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extrauser',
            old_name='icon_color',
            new_name='icon_colors',
        ),
    ]
