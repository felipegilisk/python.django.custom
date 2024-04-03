# Generated by Django 5.0.1 on 2024-04-03 15:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0008_remove_veiculo_constraint_placa_unique_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SituacaoMedicao',
            fields=[
                ('id_situacao_medicao', models.IntegerField(primary_key=True, serialize=False)),
                ('descricao_situacao_medicao', models.TextField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ApontamentoReserva',
            fields=[
                ('id_apontamento_reserva', models.IntegerField(primary_key=True, serialize=False)),
                ('data_hora_inicio', models.DateTimeField()),
                ('data_hora_termino', models.DateTimeField()),
                ('valor_mensal_considerado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_total_uso', models.DecimalField(decimal_places=2, max_digits=10)),
                ('veiculo_reserva', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Indisponibilidade',
            fields=[
                ('id_indisponibilidade', models.IntegerField(primary_key=True, serialize=False)),
                ('data_hora_inicio', models.DateTimeField()),
                ('data_hora_termino', models.DateTimeField()),
                ('valor_base_veiculo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_indisponibilidade', models.DecimalField(decimal_places=2, max_digits=10)),
                ('apontamento_reserva', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='locacao.apontamentoreserva')),
                ('unidade_indisponibilidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.unidade')),
                ('veiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.veiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Medicao',
            fields=[
                ('id_medicao', models.IntegerField(primary_key=True, serialize=False)),
                ('mes_medicao', models.DateField()),
                ('valor_parcial', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_multa', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valor_final', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unidade_medicao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.unidade')),
                ('situacao_medicao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='locacao.situacaomedicao')),
            ],
        ),
    ]
