# Generated by Django 3.1.7 on 2021-04-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('time_posted', models.DateTimeField()),
                ('message', models.TextField()),
                ('times_liked', models.PositiveIntegerField()),
                ('times_disliked', models.PositiveIntegerField()),
                ('video_id', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['times_liked'],
            },
        ),
    ]