# Generated by Django 3.1.7 on 2021-04-28 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('time_posted', models.DateTimeField()),
                ('message', models.TextField()),
                ('times_liked', models.PositiveIntegerField()),
                ('times_disliked', models.PositiveIntegerField()),
                ('original_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comments.comment')),
            ],
            options={
                'ordering': ['time_posted'],
            },
        ),
    ]