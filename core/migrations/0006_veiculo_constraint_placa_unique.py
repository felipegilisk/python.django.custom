# Generated by Django 5.0.1 on 2024-04-02 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_veiculo_unidade'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='veiculo',
            constraint=models.UniqueConstraint(fields=('placa',), name='constraint_placa_unique', violation_error_message='Já existe um veículo com esta placa!'),
        ),
    ]
