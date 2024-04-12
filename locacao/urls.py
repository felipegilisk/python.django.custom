from django.urls import path
from locacao.views import *


urlpatterns = [
    # Reservas
    path('listar_reservas/', listar_reservas, name="listar_reservas"),

    # medicao
    path('pre_medicao/', pre_medicao, name='pre_medicao'),
    path('detalhe_medicao/', detalhe_medicao, name='detalhe_medicao'),
    path('novo_apontamento/', novo_apontamento, name='novo_apontamento'),
    path('insert_indisponibilidade/', insert_indisponibilidade, name='insert_indisponibilidade'),
]
