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
    # form = Teste()
    return render(request, r'locacao\medicao\pre_medicao.html', {'form': form})


def novo_apontamento(request):
    form = None
    return render(request, r'locacao\medicao\novo_apontamento.html', {'form': form})
