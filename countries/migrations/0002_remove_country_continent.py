# Generated by Django 2.0.1 on 2018-02-23 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='continent',
        ),
    ]
