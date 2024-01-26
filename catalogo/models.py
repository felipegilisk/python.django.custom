from django.db import models

# Create your models here.
class Produto(models.Model):
    id_produto = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=250)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"({self.id_produto}) - {self.nome}"
