# Generated by Django 2.0.6 on 2020-03-11 13:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albumapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chapter',
            name='audio',
        ),
    ]
