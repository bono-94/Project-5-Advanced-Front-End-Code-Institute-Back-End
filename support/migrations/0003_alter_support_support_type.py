# Generated by Django 3.2.20 on 2023-09-20 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0002_auto_20230920_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='support_type',
            field=models.CharField(choices=[('consultacy', 'Book a Consultancy'), ('feedback', 'Feedback'), ('request', 'Request Knowledge'), ('support', 'Support Ticket'), ('suggestion', 'Suggestion')], default='support', max_length=21),
        ),
    ]