# Generated by Django 2.0.3 on 2018-08-16 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gotrees', '0008_auto_20180815_1704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trees',
            old_name='kind',
            new_name='species',
        ),
    ]