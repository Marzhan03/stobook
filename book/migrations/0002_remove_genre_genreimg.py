# Generated by Django 4.2.6 on 2023-10-23 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='genreimg',
        ),
    ]