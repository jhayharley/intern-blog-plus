# Generated by Django 2.0.4 on 2018-04-23 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='reaction',
        ),
        migrations.AlterField(
            model_name='post',
            name='comment',
            field=models.ManyToManyField(related_name='commments', to='blog.Comment'),
        ),
    ]
