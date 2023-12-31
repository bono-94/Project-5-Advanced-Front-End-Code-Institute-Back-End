# Generated by Django 3.2.20 on 2023-10-20 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20230925_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=2100),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='post_images/tree.jpg', null=True, upload_to='post_images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='sub_title',
            field=models.CharField(max_length=84, unique=False),
        ),
        migrations.AlterField(
            model_name='post',
            name='topic',
            field=models.CharField(max_length=42),
        ),
    ]
