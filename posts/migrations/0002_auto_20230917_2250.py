# Generated by Django 3.2.20 on 2023-09-17 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_filter',
        ),
        migrations.AddField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('idea', 'Idea'), ('story', 'Story'), ('journal', 'Journal'), ('blog', 'Blog')], default='idea', max_length=32),
        ),
    ]