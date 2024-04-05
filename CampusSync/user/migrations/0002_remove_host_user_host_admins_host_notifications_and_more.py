# Generated by Django 5.0.3 on 2024-04-05 12:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='user',
        ),
        migrations.AddField(
            model_name='host',
            name='admins',
            field=models.ManyToManyField(related_name='hosts_owned', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='host',
            name='notifications',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='user',
            name='notifications',
            field=models.IntegerField(default=0),
        ),
    ]
