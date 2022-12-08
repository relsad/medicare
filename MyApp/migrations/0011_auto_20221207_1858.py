# Generated by Django 2.2.5 on 2022-12-07 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0010_patient_accstatus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='accstatus',
        ),
        migrations.AddField(
            model_name='patient',
            name='martial_status',
            field=models.CharField(choices=[('Married', 'Married'), ('Single', 'Single'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed')], default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='patient',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
