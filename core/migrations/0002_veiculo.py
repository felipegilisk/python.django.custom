# Generated by Django 5.0.1 on 2024-03-26 21:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id_veiculo', models.IntegerField(primary_key=True, serialize=False)),
                ('placa', models.CharField(max_length=7)),
                ('marca_modelo', models.CharField(max_length=250)),
                ('grupo_veiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.grupoveiculo')),
            ],
        ),
    ]