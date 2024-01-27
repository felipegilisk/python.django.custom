from django.db import models


# Create your models here.
class Produto(models.Model):
    id_produto = models.IntegerField(primary_key=True)
    max_length_nome = 100
    nome = models.CharField(max_length=max_length_nome)
    max_length_descricao = 250
    descricao = models.CharField(max_length=max_length_descricao)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"({self.id_produto}) - {self.nome}"
