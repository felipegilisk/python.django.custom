from django.urls import path
from locacao.views import *


urlpatterns = [
    # Reservas
    path('listar_reservas/', listar_reservas, name="listar_reservas"),

    # medicao
    path('pre_medicao/', pre_medicao, name='pre_medicao'),
    path('detalhe_medicao/', detalhe_medicao, name='detalhe_medicao'),

    path('novo_apontamento/', nova_indisponibilidade, name='novo_apontamento'),
    path('insert_indisponibilidade/', insert_indisponibilidade, name='insert_indisponibilidade'),
    path('excluir_indisponibilidade/<int:id_indisponibilidade>', excluir_indisponibilidade, name='excluir_indisponibilidade'),
    path('delete_indisponibilidade/<int:id_indisponibilidade>', delete_indisponibilidade, name='delete_indisponibilidade'),

    path('novo_apontamento_reserva/', novo_apontamento_reserva, name='novo_apontamento_reserva'),
    path('insert_apontamento_reserva/', insert_apontamento_reserva, name='insert_apontamento_reserva'),
]
