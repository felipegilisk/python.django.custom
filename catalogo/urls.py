from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('cadastrar/', cadastrar, name="cadastrar"),
    path('insert/', insert, name="insert"),
    path('editar/<int:id_produto>', editar, name="editar"),
    path('update/<int:id_produto>', update, name="update"),
    path('delete/<int:id_produto>', deletar, name='delete')
]