from django import forms
from django.db import models
from core.models import *


### forms para unidades

class UnidadeUpdateForm(forms.ModelForm):
    class Meta:
        model = Unidade
        fields = ['codigo_unidade', 'sigla_unidade', 'descricao_unidade']
    
    def __init__(self, *args, **kwargs):
        super(UnidadeUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field, in self.fields.items():
            if field_name == "codigo_unidade":
                field.label = "Código da Unidade"
                field.widget.attrs['class'] = 'col-1'
                field.widget.attrs['min'] = '0'

            elif field_name == "sigla_unidade":
                field.label = "Sigla da Unidade"
                field.widget = forms.TextInput(
                    attrs={
                        'class': 'col-2',
                        'maxlength': '10'
                    }
                )

            elif field_name == "descricao_unidade":
                field.label = "Nome da Unidade"
                field.widget = forms.TextInput(
                    attrs={
                        'class': 'col-8',
                        'maxlength': '100'
                    }
                )


class UnidadeInsertForm(UnidadeUpdateForm):
    def __init__(self, *args, **kwargs):
        super(UnidadeInsertForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "codigo_unidade":
                field.widget.attrs['placeholder'] = '0'

            elif field_name == "sigla_unidade":
                field.widget.attrs['placeholder'] = 'sigla da unidade'

            elif field_name == "descricao_unidade":
                field.widget.attrs['placeholder'] = 'nome da unidade por extenso'


### forms para grupo de veículos

class GrupoVeiculoUpdateForm(forms.ModelForm):
    class Meta:
        model = GrupoVeiculo
        fields = ['descricao_grupo', 'valor_mensal']

    def __init__(self, *args, **kwargs):
        super(GrupoVeiculoUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "descricao_grupo":
                field.label = "Descricao"
                field.widget = forms.TextInput(
                    attrs={
                        'class': 'col-8',
                    }
                )

            elif field_name == "valor_mensal":
                field.label = "Valor Mensal"
                field.decimal_places = 2
                field.widget = forms.NumberInput(
                    attrs={
                        'class': 'col-2',
                        'step': '0.01',
                        'min': 0.00,
                    }
                )

class GrupoVeiculoInsertForm(GrupoVeiculoUpdateForm):
    def __init__(self, *args, **kwargs):
        super(GrupoVeiculoInsertForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "descricao_grupo":
                field.widget.attrs['placeholder'] = 'descricao_do_grupo'

            elif field_name == "valor_mensal":
                field.widget.attrs['placeholder'] = '0.00'


### forms para veículos

class VeiculoUpdateForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['placa', 'marca_modelo', 'grupo_veiculo', 'unidade', 'situacao']

    def __init__(self, *args, **kwargs):
        super(VeiculoUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "placa":
                field.label = "Placa"
                field.widget = forms.TextInput(
                    attrs={
                        'class': 'col-2',
                        'maxlength': '7',
                    }
                )

            elif field_name == "marca_modelo":
                field.label = "Marca/Modelo"
                field.widget = forms.TextInput(
                    attrs={
                        'class': 'col-8',
                    }
                )

            elif field_name == "grupo_veiculo":
                field.label = "Grupo de Veículos"
                field.widget.attrs['class'] = 'col-4'
            
            elif field_name == 'unidade':
                field.label = "Unidade"
                field.widget.attrs['class'] = 'col-2'

            elif field_name == "situacao":
                field.label = "Ativo"


class VeiculoInsertForm(VeiculoUpdateForm):
    def __init__(self, *args, **kwargs):
        super(VeiculoInsertForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "placa":
                field.widget.attrs['placeholder'] = 'ABC1D23'

            elif field_name == "marca_modelo":
                field.widget.attrs['placeholder'] = 'marca/modelo'
