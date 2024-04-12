from django.urls import path
from core.views import *


urlpatterns = [
    path('', home, name="home"),
    # Unidade
    path('listar_unidade/', listar_unidade, name="listar_unidade"),
    path('cadastrar_unidade/', cadastrar_unidade, name="cadastrar_unidade"),
    path('insert_unidade/', insert_unidade, name="insert_unidade"),

    # Grupo Veiculo
    path('listar_grupo_veiculo/', listar_grupo_veiculo, name="listar_grupo_veiculo"),
    path('cadastrar_grupo_veiculo/', cadastrar_grupo_veiculo, name="cadastrar_grupo_veiculo"),
    path('insert_grupo_veiculo/', insert_grupo_veiculo, name="insert_grupo_veiculo"),
    path('editar_grupo_veiculo/<int:id_grupo_veiculo>', editar_grupo_veiculo, name="editar_grupo_veiculo"),
    path('update_grupo_veiculo/<int:id_grupo_veiculo>', update_grupo_veiculo, name="update_grupo_veiculo"),
    path('excluir_grupo_veiculo/<int:id_grupo_veiculo>', excluir_grupo_veiculo, name="excluir_grupo_veiculo"),
    path('delete_grupo_veiculo/<int:id_grupo_veiculo>', delete_grupo_veiculo, name='delete_grupo_veiculo'),

    # Veiculo
    path('listar_veiculo/', listar_veiculo, name="listar_veiculo"),
    path('cadastrar_veiculo/', cadastrar_veiculo, name="cadastrar_veiculo"),
    path('insert_veiculo/', insert_veiculo, name="insert_veiculo"),
    path('editar_veiculo/<int:id_veiculo>', editar_veiculo, name="editar_veiculo"),
    path('update_veiculo/<int:id_veiculo>', update_veiculo, name="update_veiculo"),

    # dados diversos
    path('veiculo_get_valor_mensal/<int:id_veiculo>', veiculo_get_valor_mensal, name='veiculo_get_valor_mensal'),
]