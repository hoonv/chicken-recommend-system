# Generated by Django 2.2.7 on 2019-11-23 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chickens', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='photo',
            field=models.ImageField(blank=True, default='default_image.PNG', upload_to=''),
        ),
    ]