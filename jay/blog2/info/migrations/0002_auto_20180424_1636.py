# Generated by Django 2.0.4 on 2018-04-24 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='info',
            options={'ordering': ('-id',)},
        ),
    ]
