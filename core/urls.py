from django.urls import path
from core.views import *


urlpatterns = [
    path('', home, name="home"),
    path('cadastrar_grupo_veiculo/', cadastrar_grupo_veiculo, name="cadastrar_grupo_veiculo"),
    path('insert_grupo_veiculo/', insert_grupo_veiculo, name="insert_grupo_veiculo"),
    path('editar_grupo_veiculo/<int:id_grupo_veiculo>', editar_grupo_veiculo, name="editar_grupo_veiculo"),
    path('update_grupo_veiculo/<int:id_grupo_veiculo>', update_grupo_veiculo, name="update_grupo_veiculo"),
    path('excluir_grupo_veiculo/<int:id_grupo_veiculo>', excluir_grupo_veiculo, name="excluir_grupo_veiculo"),
    path('delete_grupo_veiculo/<int:id_grupo_veiculo>', delete_grupo_veiculo, name='delete_grupo_veiculo'),

    path('cadastrar_veiculo/', cadastrar_veiculo, name="cadastrar_veiculo"),
    path('insert_veiculo/', insert_veiculo, name="insert_veiculo"),
    # path('editar_veiculo/<int:id_grupo_veiculo>', editar_veiculo, name="editar_veiculo"),
    # path('update_veiculo/<int:id_grupo_veiculo>', update_veiculo, name="update_veiculo"),
    # path('excluir_veiculo/<int:id_grupo_veiculo>', excluir_veiculo, name="excluir_veiculo"),
    # path('delete_veiculo/<int:id_grupo_veiculo>', delete_veiculo, name='delete_veiculo')
]