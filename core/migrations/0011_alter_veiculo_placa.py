# Generated by Django 5.0.1 on 2024-04-21 19:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_veiculo_placa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='veiculo',
            name='placa',
            field=models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_registration', message='Insira uma placa no formato AAA1A11', regex='([A-Z]){3}([0-9])([0-9]|[A-J])([0-9]){2}'), django.core.validators.MaxLengthValidator(limit_value=7, message='A placa deve conter exatamente 7 caracteres'), django.core.validators.MinLengthValidator(limit_value=7, message='A placa deve conter exatamente 7 caracteres')]),
        ),
    ]