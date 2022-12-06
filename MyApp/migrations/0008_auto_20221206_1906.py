# Generated by Django 2.2.5 on 2022-12-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0007_auto_20221206_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='category',
            field=models.CharField(choices=[('Highest', 'Highest'), ('First', 'First'), ('Second', 'Second')], default='-', max_length=25),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='exp_years',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='rating',
            field=models.PositiveIntegerField(default=0),
        ),
    ]