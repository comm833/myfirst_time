# Generated by Django 3.0 on 2021-01-28 21:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('microblog', '0004_auto_20210128_1340'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='post',
        ),
    ]