from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('cadastrar/', cadastrar, name="cadastrar"),
    path('insert/', insert, name="insert"),
    path('editar/<int:id_produto>', editar, name="editar"),
    path('update/<int:id_produto>', update, name="update"),
    path('excluir/<int:id_produto>', excluir, name="excluir"),
    path('delete/<int:id_produto>', delete, name='delete')
]