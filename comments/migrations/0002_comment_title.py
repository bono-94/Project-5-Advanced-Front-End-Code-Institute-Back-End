# Generated by Django 3.2.20 on 2023-09-17 22:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=42),
            preserve_default=False,
        ),
    ]
