# Generated by Django 3.1.1 on 2020-11-13 14:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0021_auto_20201113_0953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentthinkuser',
            name='think',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_query_name='com_thought', to='profiles.thoughtuser'),
        ),
    ]
