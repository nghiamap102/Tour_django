# Generated by Django 3.2.5 on 2021-11-21 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0003_auto_20211121_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='views',
            name='created_date',
            field=models.DateTimeField(null=True),
        ),
    ]
