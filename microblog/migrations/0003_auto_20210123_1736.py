# Generated by Django 3.0 on 2021-01-24 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0002_auto_20210123_1733'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
