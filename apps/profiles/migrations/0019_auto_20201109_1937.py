# Generated by Django 3.1.1 on 2020-11-09 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0018_auto_20201109_1842'),
    ]

    operations = [
        migrations.AddField(
            model_name='thoughtuser',
            name='change_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='think_change_date'),
        ),
        migrations.AlterField(
            model_name='commentthinkuser',
            name='pud_date',
            field=models.DateTimeField(verbose_name='comment_think_pud_date'),
        ),
        migrations.AlterField(
            model_name='commentthinkuser',
            name='text',
            field=models.CharField(max_length=360, verbose_name='comment_think_text'),
        ),
        migrations.AlterField(
            model_name='commentthinkuser',
            name='title',
            field=models.CharField(max_length=50, verbose_name='comment_think_title'),
        ),
    ]
