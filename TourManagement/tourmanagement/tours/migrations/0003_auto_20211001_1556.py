# Generated by Django 3.2.5 on 2021-10-01 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0002_auto_20211001_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='toursdetail',
            name='imagedetail',
            field=models.ManyToManyField(blank=True, null=True, related_name='details', to='tours.ImgDetail'),
        ),
        migrations.AlterField(
            model_name='imgdetail',
            name='tourdetail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tours.toursdetail'),
        ),
    ]