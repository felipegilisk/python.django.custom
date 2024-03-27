from django import forms
from django.db import models
from core.models import *


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
        fields = ['placa', 'marca_modelo', 'grupo_veiculo']

    def __init__(self, *args, **kwargs):
        super(VeiculoUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "placa":
                field.label = "Placa"
                field.widget = forms.TextInput(
                    attrs={
                        'class': 'col-2',
                    }
                )

            elif field_name == "marca_modelo":
                field.label = "Marca/Modelo"
                field.widget = forms.TextInput(
                    attrs={
                        'class': 'col-8',
                    }
                )

            elif field_name == "marca_modelo":
                CHOICES = GrupoVeiculo.objects.all()
                field.label = "Marca/Modelo"
                field.widget = forms.ChoiceField(
                    choices=CHOICES,
                    widget=forms.Select(
                        attrs={
                            'class': 'col-4',
                        },
                    )
                )

class VeiculoInsertForm(VeiculoUpdateForm):
    def __init__(self, *args, **kwargs):
        super(VeiculoInsertForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "placa":
                field.widget.attrs['placeholder'] = 'ABC1D23'

            elif field_name == "marca_modelo":
                field.widget.attrs['placeholder'] = 'marca/modelo'
