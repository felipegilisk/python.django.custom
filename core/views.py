from django.shortcuts import render, redirect
from django.contrib import messages
from core.models import *
from core.forms import *


### PÁGINA INICIAL
def home(request):
    if request.path == '/':
        return redirect('')
    grupo_veiculos = GrupoVeiculo.objects.all()
    return render(request, r"core\index.html", {"grupo_veiculos": grupo_veiculos})


### GRUPOS DE VEÍCULOS

def listar_grupo_veiculo(request):
    grupo_veiculos = GrupoVeiculo.objects.all()
    return render(request, r"core\grupo_veiculo\listar_grupo_veiculo.html", {"grupo_veiculos": grupo_veiculos})


def cadastrar_grupo_veiculo(request):
    form = GrupoVeiculoInsertForm()
    return render(request, r"core\grupo_veiculo\cadastrar_grupo_veiculo.html", {'form': form})


def insert_grupo_veiculo(request):
    if request.method == 'POST':
        form = GrupoVeiculoUpdateForm(request.POST)
        if form.is_valid():
            descricao_grupo = form['descricao_grupo'].value()
            valor_mensal = form['valor_mensal'].value()
            
            if float(valor_mensal) < 0:
                messages.error(
                    request,
                    f"Campo [ Valor Mensal ] deve conter um valor de no mínimo 0.00"
                )
            else:
                GrupoVeiculo.objects.create(
                    descricao_grupo = descricao_grupo,
                    valor_mensal = valor_mensal
                )
                messages.success(
                    request,
                    "Grupo de Veículos cadastrado com sucesso!"
                )
        else:
            messages.error(request, "Dados do formulário inválidos")

    return redirect(listar_grupo_veiculo)


def editar_grupo_veiculo(request, id_grupo_veiculo):
    grupo_veiculo = GrupoVeiculo.objects.get(id_grupo_veiculo=id_grupo_veiculo)
    form = GrupoVeiculoUpdateForm(instance=grupo_veiculo)

    return render(request, r'core\grupo_veiculo\atualizar_grupo_veiculo.html', {"grupo_veiculo": grupo_veiculo, "form": form})


def update_grupo_veiculo(request, id_grupo_veiculo):
    grupo_veiculo = GrupoVeiculo.objects.get(id_grupo_veiculo=id_grupo_veiculo)
    form = GrupoVeiculoUpdateForm(request.POST, instance=grupo_veiculo)
    if request.method == 'POST':
        if form.is_valid():
            descricao_grupo = form['descricao_grupo'].value()
            valor_mensal = form['valor_mensal'].value()

            if float(valor_mensal) < 0:
                messages.error(
                    request,
                    f"Campo [Preço] deve conter um valor de no mínimo 0.00"
                )
            else:
                grupo_veiculo.descricao_grupo = descricao_grupo
                grupo_veiculo.valor_mensal = valor_mensal
                grupo_veiculo.save()
                messages.success(
                    request,
                    f"Grupo de Veículos código {grupo_veiculo.id_grupo_veiculo} atualizado com sucesso!"
                )
        else:
            messages.error(request, "Dados do formulário inválidos")

    return redirect(listar_grupo_veiculo)


def excluir_grupo_veiculo(request, id_grupo_veiculo):
    grupo_veiculo = GrupoVeiculo.objects.get(id_grupo_veiculo=id_grupo_veiculo)
    return render(request, r'core\grupo_veiculo\deletar_grupo_veiculo.html', {'grupo_veiculo': grupo_veiculo})


def delete_grupo_veiculo(request, id_grupo_veiculo):
    grupo_veiculo = GrupoVeiculo.objects.get(id_grupo_veiculo=id_grupo_veiculo)
    if request.method == 'POST':
        grupo_veiculo.delete()
        messages.success(
            request,
            f"Grupo de Veículos código {id_grupo_veiculo} excluído com sucesso!"
        )
    return redirect(listar_grupo_veiculo)


### VEÍCULOS

def listar_veiculo(request):
    if request.path == '/':
        return redirect('')
    veiculos = Veiculo.objects.all()
    return render(request, r"core\veiculo\listar_veiculo.html", {"veiculos": veiculos})


def cadastrar_veiculo(request):
    form = VeiculoInsertForm()
    return render(request, r"core\veiculo\cadastrar_veiculo.html", {'form': form})


def insert_veiculo(request):
    if request.method == 'POST':
        form = VeiculoUpdateForm(request.POST)
        if form.is_valid():
            placa = form['placa'].value().upper()
            marca_modelo = form['marca_modelo'].value()
            grupo_veiculo = GrupoVeiculo.objects.get(pk=form['grupo_veiculo'].value())
            
            if len(placa) != 7:
                messages.error(
                    request,
                    f"Campo [ Placa ] deve conter exatamente 7 caracteres"
                )
            
            elif len(marca_modelo) == 0:
                messages.error(
                    request,
                    f"Campo [ Marca/Modelo ] não pode ficar em branco"
                )

            else:
                Veiculo.objects.create(
                    placa = placa,
                    marca_modelo = marca_modelo,
                    grupo_veiculo = grupo_veiculo

                )
                messages.success(
                    request,
                    "Veículo cadastrado com sucesso!"
                )
        else:
            messages.error(request, "Dados do formulário inválidos")

    return redirect(listar_veiculo)


def editar_veiculo(request, id_veiculo):
    veiculo = Veiculo.objects.get(id_veiculo=id_veiculo)
    form = VeiculoUpdateForm(instance=veiculo)

    return render(request, r'core\veiculo\atualizar_veiculo.html', {"veiculo": veiculo, "form": form})


def update_veiculo(request, id_veiculo):
    veiculo = Veiculo.objects.get(id_veiculo=id_veiculo)
    form = VeiculoUpdateForm(request.POST, instance=veiculo)
    redir = request.META.get('HTTP_REFERER')

    if request.method == 'POST':
        if form.is_valid():
            placa = form['placa'].value().upper()
            marca_modelo = form['marca_modelo'].value()

            if len(placa) != 7:
                messages.error(
                    request,
                    f"Campo [ Placa ] estar no formato AAA1X11!"
                )
            elif len(marca_modelo) == 0:
                messages.error(
                    request,
                    f"Campo [ Marca / Modelo ] deve ser preenchido!"
                )
            else:
                veiculo.placa = placa
                veiculo.marca_modelo = marca_modelo
                veiculo.save()
                messages.success(
                    request,
                    f"Veículo código {veiculo.id_veiculo} atualizado com sucesso!"
                )
                redir = listar_veiculo
        else:
            messages.error(request, "Dados do formulário inválidos")

    return redirect(redir)


def excluir_veiculo(request, id_veiculo):
    veiculo = Veiculo.objects.get(id_veiculo=id_veiculo)
    return render(request, r'core\veiculo\deletar_veiculo.html', {'veiculo': veiculo})


def delete_veiculo(request, id_veiculo):
    veiculo = Veiculo.objects.get(id_veiculo=id_veiculo)
    if request.method == 'POST':
        veiculo.delete()
        messages.success(
            request,
            f"Veículo código {id_veiculo} excluído com sucesso!"
        )
    return redirect(listar_veiculo)