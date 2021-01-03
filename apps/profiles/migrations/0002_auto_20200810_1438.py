# Generated by Django 3.0.3 on 2020-08-10 09:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlreadyIp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_name', models.CharField(max_length=50, verbose_name='ip_name')),
            ],
        ),
        migrations.RenameModel(
            old_name='ThinkUser',
            new_name='ThoughtUser',
        ),
    ]
