# Generated by Django 2.2.5 on 2022-12-07 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0013_auto_20221207_2035'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(default=None, upload_to='image/'),
        ),
    ]