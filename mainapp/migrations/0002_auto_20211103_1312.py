# Generated by Django 3.2.8 on 2021-11-03 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homebackground',
            name='subtitle',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='homebackground',
            name='title',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
