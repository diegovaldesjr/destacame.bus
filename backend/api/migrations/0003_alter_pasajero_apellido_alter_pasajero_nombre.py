# Generated by Django 4.0 on 2021-12-29 03:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_reserva_pasajero'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pasajero',
            name='apellido',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]+$', 'Only letters and spaces are allowed in the Location Name.')]),
        ),
        migrations.AlterField(
            model_name='pasajero',
            name='nombre',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]+$', 'Only letters and spaces are allowed in the Location Name.')]),
        ),
    ]
