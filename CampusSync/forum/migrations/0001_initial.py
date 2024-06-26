# Generated by Django 5.0.3 on 2024-04-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('answer', models.TextField()),
                ('answered_by_host', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('question', models.TextField()),
                ('is_answered', models.BooleanField(default=False)),
            ],
        ),
    ]
