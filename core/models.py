from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator


class Unidade(models.Model):
    id_unidade = models.IntegerField(primary_key=True)
    sigla_unidade = models.TextField(max_length=10, null=False)
    descricao_unidade = models.TextField(max_length=100, null=False)

    def __str__(self):
        return f"{str(self.id_unidade).zfill(2)} - {self.sigla_unidade}"


class GrupoVeiculo(models.Model):
    id_grupo_veiculo = models.IntegerField(primary_key=True)
    descricao_grupo = models.CharField(max_length=250)
    valor_mensal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.id_grupo_veiculo} - {self.descricao_grupo}'


class Veiculo(models.Model):
    id_veiculo = models.IntegerField(primary_key=True)
    placa = models.CharField(
        max_length=7,
        unique=True,
        validators = [
            RegexValidator(
                regex='^([A-Z]){3}(\d){1}([A-Z]|\d){1}(\d){2}',
                message="Insira uma placa no formato AAA1A11",
                code="invalid_registration"
                ),
            MaxLengthValidator(
                limit_value=7,
                message="A placa deve conter exatamente 7 caracteres",
                ),
            MinLengthValidator(
                limit_value=7,
                message="A placa deve conter exatamente 7 caracteres",
                ),
            ]
        )
    marca_modelo = models.CharField(max_length=250)
    grupo_veiculo = models.ForeignKey(GrupoVeiculo, on_delete=models.PROTECT)
    situacao = models.BooleanField(default=True)
    unidade = models.ForeignKey(Unidade, on_delete=models.PROTECT, default=0)

    def __str__(self):
        return f"{self.placa} - {self.marca_modelo}"

