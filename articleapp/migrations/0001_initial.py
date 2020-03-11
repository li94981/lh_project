# Generated by Django 2.0.6 on 2020-03-10 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mrticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('create_date', models.DateField(blank=True, null=True)),
                ('publish_date', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='static/img')),
                ('upload_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_pic',
            },
        ),
    ]