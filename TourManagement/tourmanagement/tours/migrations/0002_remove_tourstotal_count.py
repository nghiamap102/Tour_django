# Generated by Django 3.2.5 on 2021-08-09 01:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourstotal',
            name='count',
        ),
    ]
