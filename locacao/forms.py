from datetime import date, timedelta
from django import forms
from locacao.models import *
from core.models import Unidade


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

