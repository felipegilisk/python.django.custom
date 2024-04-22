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
    
    indisp = IndisponibilidadeSerializer()
    indisp.start_date = datetime(day=1, month=mes, year=ano)
    if mes == 12:
        indisp.end_date = datetime(day=1, month=1, year=ano+1) - timedelta(microseconds=1)
    else:
        indisp.end_date = datetime(day=1, month=mes+1, year=ano) - timedelta(microseconds=1)

    i = indisp.get_results()
    v_total = 0
    for item in i:
        item['inicio'] = datetime.fromisoformat(item['inicio']).strftime('%d/%m/%Y %H:%M')
        item['termino'] = datetime.fromisoformat(item['termino']).strftime('%d/%m/%Y %H:%M')
        v_total += item['valor']
    
    dados = {
        'data_medicao': data_medicao,
        'unidade': unidade,
        'indisp_ser': dumps(i),
        'teste': i,
        'total': v_total,
    }
    return render(request, r"locacao\medicao\detalhe_medicao.html", dados)


def nova_indisponibilidade(request):
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

    return render(request, r'locacao\medicao\nova_indisponibilidade.html', {'form': form})


def insert_indisponibilidade(request):
    rtrn = redirect(pre_medicao)
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
            apontamento_reserva = None
            status = False
            
            indisp = Indisponibilidade.objects.create(
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

            if tem_reserva is True:
                rtrn = novo_apontamento_reserva(request, indisp)

        else:
            for error in form.errors.keys():
                messages.error(request, form.errors[error])
    
    return rtrn


def novo_apontamento_reserva(request, indisponibilidade: Indisponibilidade):
    form = ApontamentoReservaInsertForm()
    for field_name, field in form.fields.items():
        if 'data' in field_name:
            field.widget.attrs['min'] = indisponibilidade.data_hora_inicio
            field.widget.attrs['max'] = indisponibilidade.data_hora_termino
        
        elif field_name == "valor_total_uso":
            field.widget.attrs['readonly'] = ""

    return render(request, r'locacao\medicao\novo_apontamento_reserva.html', {'form': form, 'indisponibilidade': indisponibilidade})


def insert_apontamento_reserva(request):
    if request.method == 'POST':
        form = ApontamentoReservaInsertForm(request.POST)
        if form.is_valid():
            veiculo_reserva = Veiculo.objects.get(id_veiculo=int(form['veiculo_reserva'].value()))
            data_hora_inicio = datetime.fromisoformat(form['data_hora_inicio'].value())
            data_hora_termino = datetime.fromisoformat(form['data_hora_termino'].value())
            valor_mensal_considerado = float(form['valor_mensal_considerado'].value())
            valor_total_uso = float(form['valor_mensal_considerado'].value())
            
            apontamento_reserva = ApontamentoReserva.objects.create(
                veiculo_reserva = veiculo_reserva,
                data_hora_inicio = data_hora_inicio,
                data_hora_termino = data_hora_termino,
                valor_mensal_considerado = valor_mensal_considerado,
                valor_total_uso = valor_total_uso
            )

            indisponibilidade = Indisponibilidade.objects.get(id_indisponibilidade=int(form['indisponibilidade'].value()))
            indisponibilidade.tem_reserva = 1
            indisponibilidade.apontamento_reserva = apontamento_reserva
            indisponibilidade.save()

        else:
            for error in form.errors.keys():
                messages.error(request, form.errors[error])

    return redirect(pre_medicao)


def excluir_indisponibilidade(request, id_indisponibilidade):
    indisponibilidade = Indisponibilidade.objects.get(id_indisponibilidade=id_indisponibilidade)
    total_tempo = indisponibilidade.data_hora_termino - indisponibilidade.data_hora_inicio
    total_horas = total_tempo.total_seconds()//(60*60)

    return render(request, r'locacao\medicao\deletar_indisponibilidade.html', {'indisponibilidade': indisponibilidade, 'total_horas': total_horas})


def delete_indisponibilidade(request, id_indisponibilidade):
    indisponibilidade = Indisponibilidade.objects.get(id_indisponibilidade=id_indisponibilidade)
    if request.method == 'POST':
        indisponibilidade.delete()
        messages.success(
                request,
                f"Indisponibilidade excluída com sucesso!"
            )

    return redirect(pre_medicao)
