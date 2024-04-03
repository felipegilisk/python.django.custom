from django.db import models
from core.models import Veiculo, Unidade


class SituacaoMedicao(models.Model):
    id_situacao_medicao = models.IntegerField(primary_key=True)
    descricao_situacao_medicao = models.TextField(max_length=50, unique=True)

    def __str__(self):
        return self.descricao_situacao_medicao


class Medicao(models.Model):
    id_medicao = models.IntegerField(primary_key=True)
    mes_medicao = models.DateField()
    situacao_medicao = models.ForeignKey(SituacaoMedicao, on_delete=models.PROTECT)
    unidade_medicao = models.ForeignKey(Unidade, on_delete=models.PROTECT)
    valor_parcial = models.DecimalField(max_digits=10, decimal_places=2)
    valor_multa = models.DecimalField(max_digits=10, decimal_places=2)
    valor_final = models.DecimalField(max_digits=10, decimal_places=2)


class ApontamentoReserva(models.Model):
    id_apontamento_reserva = models.IntegerField(primary_key=True)
    veiculo_reserva = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    data_hora_inicio = models.DateTimeField()
    data_hora_termino = models.DateTimeField()
    valor_mensal_considerado = models.DecimalField(max_digits=10, decimal_places=2)
    valor_total_uso = models.DecimalField(max_digits=10, decimal_places=2)


class Indisponibilidade(models.Model):
    id_indisponibilidade = models.IntegerField(primary_key=True)
    unidade_indisponibilidade = models.ForeignKey(Unidade, on_delete=models.PROTECT)
    data_hora_inicio = models.DateTimeField()
    data_hora_termino = models.DateTimeField()
    veiculo = models.ForeignKey(Veiculo, on_delete=models.PROTECT)
    valor_base_veiculo = models.DecimalField(max_digits=10, decimal_places=2)
    valor_indisponibilidade = models.DecimalField(max_digits=10, decimal_places=2)
    apontamento_reserva = models.ForeignKey(ApontamentoReserva, null=True, on_delete=models.SET_NULL)

