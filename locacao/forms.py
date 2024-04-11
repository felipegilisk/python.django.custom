from datetime import date, timedelta
from django import forms
from locacao.models import *
from core.models import Unidade
from setup.models import DateTimeLocalInput


### forms para medicao

class MedicaoFilterForm(forms.ModelForm):
    class Meta:
        model = Medicao
        fields = ['mes_medicao', 'unidade_medicao']

    def __init__(self, *args, **kwargs):
        super(MedicaoFilterForm, self).__init__(*args, **kwargs)
        for field_name, field, in self.fields.items():
            if field_name == "mes_medicao":
                field.label = "Mês de referência"
                field.widget = forms.widgets.SelectDateWidget(
                    empty_label=("Ano", "Mês", "Dia"),
                    years=list(range(2023, date.today().year+1)),
                    attrs={
                        'class': 'col-2 mx-1',
                    }
                )
                hoje = date.today()
                if hoje.day > 5:
                    field.initial = hoje.replace(day=1)
                else:
                    field.initial = (hoje.replace(day=1) - timedelta(days=1)).replace(day=1)

            elif field_name == "unidade_medicao":
                field.label = "Unidade"
                field.widget.attrs['class'] = 'col-2'
                # Somente unidades que possuem veículos
                field.queryset = Unidade.objects.filter(veiculo__situacao=True).exclude(id_unidade=0).distinct()


class ApontamentoReservaInsertForm(forms.ModelForm):
    class Meta:
        model = ApontamentoReserva
        fields = [
            "veiculo_reserva",
            "data_hora_inicio",
            "data_hora_termino",
            "valor_mensal_considerado",
            "valor_total_uso"
        ]
    
    def __init__(self, *args, **kwargs):
        super(ApontamentoReservaInsertForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "veiculo_reserva":
                field.label = "Veículo Reserva"
                field.widget.attrs['class'] = 'col-4'
                field.queryset = Veiculo.objects.filter(unidade_id=0, situacao=1)

            elif field_name == "data_hora_inicio":
                field.label = "Início"
                field.widget = DateTimeLocalInput()
                field.widget.attrs['class'] = 'col-3'
            
            elif field_name == "data_hora_termino":
                field.label = "Término"
                field.widget = DateTimeLocalInput()
                field.widget.attrs['class'] = 'col-3'


class IndisponibilidadeUpdateForm(forms.ModelForm):
    apontamento_reserva = ApontamentoReservaInsertForm()
    class Meta:
        model = Indisponibilidade
        fields = [
            'unidade_indisponibilidade',
            'data_hora_inicio',
            'data_hora_termino',
            'veiculo',
            'valor_base_veiculo',
            'valor_indisponibilidade',
            'tem_reserva',
        ]
        

    def __init__(self, *args, **kwargs):
        super(IndisponibilidadeUpdateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == "unidade_indisponibilidade":
                field.label = "Unidade"
                field.widget.attrs['class'] = 'col-2'
                field.queryset = Unidade.objects.filter(veiculo__situacao=True).exclude(id_unidade=0).distinct()

            elif field_name == "data_hora_inicio":
                field.label = "Início"
                field.widget = DateTimeLocalInput()
                field.widget.attrs['class'] = 'col-3'

            elif field_name == "data_hora_termino":
                field.label = "Término"
                field.widget = DateTimeLocalInput()
                field.widget.attrs['class'] = 'col-3'

            elif field_name == "veiculo":
                field.label = "Veículo"
                field.widget.attrs['class'] = 'col-4'
                field.queryset = Veiculo.objects.exclude(unidade_id=0, situacao=1)
            
            elif field_name == "tem_reserva":
                field.label = "Veículo reserva fornecido?"
                field.widget.attrs['class'] = 'form-check-input'
            
            elif field_name == "apontamento_reserva":
                field.required = False


    def clean(self):
        cleaned_data = super().clean()
        veiculo = cleaned_data.get('veiculo')

        if veiculo:
            valor_mensal = veiculo.grupo_veiculo.valor_mensal
            cleaned_data['valor_base_veiculo'] = valor_mensal

        return cleaned_data


class IndisponibilidadeInsertForm(IndisponibilidadeUpdateForm):
    def __init__(self, *args, **kwargs):
        super(IndisponibilidadeInsertForm, self).__init__(*args, **kwargs)

