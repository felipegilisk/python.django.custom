from django.db import models, connection
from core.models import Veiculo, Unidade, UnidadeSerializer, VeiculoSerializer
from rest_framework import serializers
from datetime import datetime, timedelta


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
    valor_base_veiculo = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    valor_indisponibilidade = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    tem_reserva = models.BooleanField(default=False)
    apontamento_reserva = models.ForeignKey(ApontamentoReserva, null=True, blank=True, on_delete=models.SET_NULL, default=None)
    status = models.BooleanField(default=False)



########################################
###### Serializer
########################################

class IndisponibilidadeSerializer(): # serializers.ModelSerializer):
    def __init__(self) -> None:
        self.sql = """
            SELECT * FROM (
                SELECT
                    null                                                                                AS 'id_edit',
                    cv.unidade_id 																		AS 'unidade',
                    'Base' 																				AS 'tipo',
                    cv.id_veiculo 																		AS 'id_veiculo_base',
                    cv.placa 																			AS 'placa',
                    cv.marca_modelo 																	AS 'marca_modelo',
                    cg.id_grupo_veiculo || ' - ' || cg.descricao_grupo  								AS 'grupo',
                    %s														                            AS 'inicio',
                    %s														                            AS 'termino',
                    720																					AS 'total_horas',
                    cg.valor_mensal 																	AS 'valor'
                FROM core_veiculo cv
                LEFT JOIN core_grupoveiculo cg ON cv.grupo_veiculo_id = cg.id_grupo_veiculo
                WHERE cv.unidade_id = %s
                
                UNION
                
                SELECT
                    li.id_indisponibilidade                                                             AS 'id_edit',
                    li.unidade_indisponibilidade_id 													AS 'unidade',
                    'Indisponibilidade'																	AS 'tipo',
                    li.veiculo_id 																		AS 'id_veiculo_base',
                    cv.placa 																			AS 'placa',
                    cv.marca_modelo 																	AS 'marca_modelo',
                    cg.id_grupo_veiculo || ' - ' || cg.descricao_grupo  								AS 'grupo',
                    li.data_hora_inicio 																AS 'inicio',
                    li.data_hora_termino																AS 'termino',
                    ROUND((JULIANDAY(li.data_hora_termino) - JULIANDAY(li.data_hora_inicio))*24, 0)		AS 'total_horas',
                    li.valor_indisponibilidade * -1 													AS 'valor'
                FROM locacao_indisponibilidade li
                LEFT JOIN core_veiculo cv ON li.veiculo_id = cv.id_veiculo
                LEFT JOIN core_grupoveiculo cg ON cv.grupo_veiculo_id = cg.id_grupo_veiculo
                WHERE cv.unidade_id = %s AND
                    li.data_hora_inicio >= %s AND
                    li.data_hora_termino <= %s
                
                UNION
                
                SELECT
                    la.id_apontamento_reserva                                                           AS 'id_edit',
                    li.unidade_indisponibilidade_id 													AS 'unidade',
                    'Reserva'																			AS 'tipo',
                    li.veiculo_id 																		AS 'id_veiculo_base',
                    cv.placa 																			AS 'placa',
                    cv.marca_modelo 																	AS 'marca_modelo',
                    cg.id_grupo_veiculo || ' - ' || cg.descricao_grupo  								AS 'grupo',
                    la.data_hora_inicio 																AS 'inicio',
                    la.data_hora_termino																AS 'termino',
                    ROUND((JULIANDAY(la.data_hora_termino) - JULIANDAY(la.data_hora_inicio))*24, 0)		AS 'total_horas',
                    la.valor_total_uso																	AS 'valor'
                FROM locacao_indisponibilidade li 
                RIGHT JOIN locacao_apontamentoreserva la ON li.apontamento_reserva_id = la.id_apontamento_reserva 
                LEFT JOIN core_veiculo cv ON la.veiculo_reserva_id = cv.id_veiculo
                LEFT JOIN core_grupoveiculo cg ON cv.grupo_veiculo_id = cg.id_grupo_veiculo
                WHERE li.unidade_indisponibilidade_id = %s AND
                    li.data_hora_inicio >= %s AND
                    li.data_hora_termino <= %s
            )
            ORDER BY unidade, id_veiculo_base, tipo"""

        self.start_date = datetime.today().replace(day=1, hour=0, minute=0, microsecond=0)
        self.end_date = ((self.start_date + timedelta(days=35)).replace(day=1)) - timedelta(days=1)
        self.unidade = 1

    def get_results(self):
        with connection.cursor() as cursor:
            cursor.execute(self.sql, [
                self.start_date,
                self.end_date,
                self.unidade,
                self.unidade,
                self.start_date,
                self.end_date,
                self.unidade,
                self.start_date,
                self.end_date])
            cols = [col[0] for col in cursor.description]
            r = [{col: str(value) if isinstance(value, datetime) else value for col, value in zip(cols, row)} for row in cursor.fetchall()]

        return r
    
