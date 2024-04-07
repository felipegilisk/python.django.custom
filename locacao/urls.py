from django.urls import path
from locacao.views import *


urlpatterns = [
    # Reservas
    path('listar_reservas/', listar_reservas, name="listar_reservas"),
    path('pre_medicao/', pre_medicao, name='pre_medicao'),
    path('busca_medicao/', busca_medicao, name='busca_medicao'),
    path('novo_apontamento/', novo_apontamento, name='novo_apontamento'),

]