# Generated by Django 3.2.5 on 2021-12-28 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_auto_20211225_1753'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='activeStaff',
            field=models.BooleanField(default=False),
        ),
    ]
