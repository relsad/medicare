# Generated by Django 2.2.5 on 2022-12-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0017_auto_20221208_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='photo_URI',
            field=models.CharField(default='/image/default.png', max_length=500),
        ),
    ]
