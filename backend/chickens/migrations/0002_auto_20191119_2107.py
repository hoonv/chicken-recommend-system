# Generated by Django 2.2.7 on 2019-11-19 12:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chickens', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chicken',
            old_name='content',
            new_name='desc',
        ),
    ]