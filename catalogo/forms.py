from django import forms
from django.db import models
from catalogo.models import Produto


class ProdutoUpdateForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'descricao', 'preco']

    def __init__(self, *args, **kwargs):
        super(ProdutoUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "nome":
                field.label = "Nome"
                field.widget = forms.TextInput(
                    attrs={
                        'class': 'col-8',
                    }
                )

            elif field_name == "descricao":
                field.label = "Descrição"
                field.widget = forms.Textarea(
                    attrs={
                        'class': 'col-8',
                        'rows': 3,
                    }
                )

            elif field_name == "preco":
                field.label = "Preço"
                field.decimal_places = 2
                field.widget = forms.NumberInput(
                    attrs={
                        'class': 'col-2',
                        'step': '0.01',
                        'min': 0.00,
                    }
                )

class ProdutoInsertForm(ProdutoUpdateForm):
    def __init__(self, *args, **kwargs):
        super(ProdutoInsertForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "nome":
                field.widget.attrs['placeholder'] = 'nome_do_produto'

            elif field_name == "descricao":
                field.widget.attrs['placeholder'] = 'descrição_do_produto'

            elif field_name == "preco":
                field.widget.attrs['placeholder'] = '0.00'
