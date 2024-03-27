from django.db import models


class GrupoVeiculo(models.Model):
    id_grupo_veiculo = models.IntegerField(primary_key=True)
    descricao_grupo = models.CharField(max_length=250)
    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"({self.id_grupo_veiculo}) - {self.descricao_grupo}"


class Veiculo(models.Model):
    id_veiculo = models.IntegerField(primary_key=True)
    placa = models.CharField(max_length=7)
    marca_modelo = models.CharField(max_length=250)
    grupo_veiculo = models.ForeignKey(GrupoVeiculo, on_delete=models.PROTECT)
    situacao = models.BooleanField(default=True)

    def __str__(self):
        return f"({self.id_veiculo}) - {self.placa}"
