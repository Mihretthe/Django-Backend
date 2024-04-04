# Generated by Django 5.0.3 on 2024-04-03 19:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0002_initial'),
        ('forum', '0001_initial'),
        ('user', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='answering_host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answering_host', to='user.host'),
        ),
        migrations.AddField(
            model_name='answer',
            name='answering_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answering_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='question',
            name='asker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_question_asker', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='forum',
            name='questions',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forum_questions', to='forum.question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_of_answer', to='forum.question'),
        ),
        migrations.CreateModel(
            name='EventForum',
            fields=[
                ('forum_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='forum.forum')),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
            bases=('forum.forum',),
        ),
    ]