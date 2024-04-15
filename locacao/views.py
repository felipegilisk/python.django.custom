from datetime import date, datetime
from json import dumps
from django.shortcuts import render, redirect
from django.contrib import messages
from locacao.models import *
from core.models import *
from core.utils import *
from locacao.forms import *


def listar_reservas(request):
    if request.path == '/':
        return redirect('')
    veiculos = Veiculo.objects.filter(unidade_id=0)
    return render(request, r"locacao\reservas\listar_reservas.html", {"veiculos": veiculos})


def pre_medicao(request):
    form = MedicaoFilterForm()
    return render(request, r'locacao\medicao\pre_medicao.html', {'form': form})


def detalhe_medicao(request, id_unidade=None):
    if id_unidade is not None:
        unidade = Unidade.objects.get(id_unidade=id_unidade)
    else:
        unidade = Unidade.objects.get(id_unidade=int(request.GET.get("unidade_medicao")))
    mes = int(request.GET.get("mes_medicao_month"))
    ano = int(request.GET.get("mes_medicao_year"))
    data_medicao = date(day=1, month=mes, year=ano)
    medicao = Medicao.objects.filter(mes_medicao=data_medicao, unidade_medicao=unidade)
    veiculos = Veiculo.objects.filter(unidade=unidade, situacao=1)
    indisponibilidades = Indisponibilidade.objects.filter(unidade_indisponibilidade=unidade, status=0)

    veiculo_serializer = VeiculoSerializer(veiculos, many=True)
    veiculo_serialized_data = veiculo_serializer.data

    # indisp_serializer = IndisponibilidadeSerializer(indisponibilidades, many=True)
    # indisp_serialized_data = indisp_serializer.data
    indisp = IndisponibilidadeSerializer()
    indisp.start_date = datetime(day=1, month=mes, year=ano)
    if mes == 12:
        indisp.end_date = datetime(day=1, month=1, year=ano+1) - timedelta(microseconds=1)
    else:
        indisp.end_date = datetime(day=1, month=mes+1, year=ano) - timedelta(microseconds=1)

    i = indisp.get_results()
    
    dados = {
        'medicao': medicao,
        'veiculos': veiculos,
        'data_medicao': data_medicao,
        'unidade': unidade,
        # 'veic_ser': dumps(veiculo_serialized_data),
        'indisp_ser': dumps(i)
    }
    return render(request, r"locacao\medicao\detalhe_medicao.html", dados)


def novo_apontamento(request):
    id_unidade = int(request.GET.get("unidade_medicao"))
    data_medicao = request.GET.get("data_medicao").split(' de ')
    data_medicao = datetime(day=1, month=get_month_by_name(data_medicao[1]), year=int(data_medicao[-1]))
    form = IndisponibilidadeInsertForm()
    for field_name, field in form.fields.items():
        if field_name == "unidade_indisponibilidade":
            field.queryset = Unidade.objects.filter(id_unidade=id_unidade)
            field.empty_label = None
        elif field_name == 'veiculo':
            field.queryset = Veiculo.objects.filter(unidade_id=id_unidade).exclude(situacao=0)
        elif 'data' in field_name:
            field.widget.attrs['min'] = data_medicao.isoformat()
            field.widget.attrs['max'] = datetime.today().isoformat()[:19]

    return render(request, r'locacao\medicao\novo_apontamento.html', {'form': form})


def insert_indisponibilidade(request):
    if request.method == 'POST':
        form = IndisponibilidadeInsertForm(request.POST)
        if form.is_valid():
            unidade_indisponibilidade = form['unidade_indisponibilidade'].value()
            data_hora_inicio = datetime.fromisoformat(form['data_hora_inicio'].value())
            data_hora_termino = datetime.fromisoformat(form['data_hora_termino'].value())
            veiculo = form['veiculo'].value()
            valor_base_veiculo = form.cleaned_data['valor_base_veiculo']
            tempo_indisp = (data_hora_termino - data_hora_inicio)
            horas_indisp = tempo_indisp.days*24 + tempo_indisp.seconds//3600
            valor_indisponibilidade = (valor_base_veiculo/720)*horas_indisp
            tem_reserva = form['tem_reserva'].value()
            if tem_reserva is False:
                apontamento_reserva = None
            else:
                print(tem_reserva)
                apontamento_reserva = form['apontamento_reserva'].value()
            status = False
            
            Indisponibilidade.objects.create(
                unidade_indisponibilidade = Unidade.objects.get(id_unidade=unidade_indisponibilidade),
                data_hora_inicio = data_hora_inicio,
                data_hora_termino = data_hora_termino,
                veiculo = Veiculo.objects.get(id_veiculo=veiculo),
                valor_base_veiculo = valor_base_veiculo,
                valor_indisponibilidade = valor_indisponibilidade,
                tem_reserva = tem_reserva,
                apontamento_reserva = apontamento_reserva,
                status = status
            )

        else:
            for error in form.errors.keys():
                messages.error(request, form.errors[error])
    
    return redirect(pre_medicao)
