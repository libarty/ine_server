# Generated by Django 3.0.3 on 2020-08-31 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_auto_20200814_0939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrauser',
            name='progress',
            field=models.ManyToManyField(blank=True, to='profiles.Progress'),
        ),
    ]