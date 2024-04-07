from datetime import date
from json import dumps
from django.shortcuts import render, redirect
from django.contrib import messages
from locacao.models import *
from core.models import *
from locacao.forms import *


def listar_reservas(request):
    if request.path == '/':
        return redirect('')
    veiculos = Veiculo.objects.filter(unidade_id=0)
    return render(request, r"locacao\reservas\listar_reservas.html", {"veiculos": veiculos})


def pre_medicao(request):
    form = MedicaoFilterForm()
    return render(request, r'locacao\medicao\pre_medicao.html', {'form': form})


def busca_medicao(request):
    unidade = Unidade.objects.get(id_unidade=int(request.GET.get("unidade_medicao")))
    mes = int(request.GET.get("mes_medicao_month"))
    ano = int(request.GET.get("mes_medicao_year"))
    data_medicao = date(day=1, month=mes, year=ano)
    medicao = Medicao.objects.filter(mes_medicao=data_medicao, unidade_medicao=unidade)
    veiculos = Veiculo.objects.filter(unidade=unidade, situacao=1)

    serializer = VeiculoSerializer(veiculos, many=True)
    serialized_data = serializer.data

    dados = {
        'medicao': medicao,
        'veiculos': veiculos,
        'data_medicao': data_medicao,
        'unidade': unidade,
        'veic_ser': dumps(serialized_data),
    }
    return render(request, r"locacao\medicao\busca_medicao.html", dados)
# ('json', veiculos + GrupoVeiculo.objects.all(), use_natural_foreign_keys=True)

def novo_apontamento(request):
    form = None
    return render(request, r'locacao\medicao\novo_apontamento.html', {'form': form})
