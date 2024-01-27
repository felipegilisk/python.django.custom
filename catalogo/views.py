from django.shortcuts import render, redirect
from django.contrib import messages
from catalogo.models import *
from catalogo.forms import *


# Create your views here.
def home(request):
    if request.path == '/':
        return redirect('')
    produtos = Produto.objects.all()
    return render(request, r"catalogo\index.html", {"produtos": produtos})


def cadastrar(request):
    form = ProdutoInsertForm()
    return render(request, r"catalogo\cadastrar.html", {'form': form})


def insert(request):
    if request.method == 'POST':
        form = ProdutoUpdateForm(request.POST)
        if form.is_valid():
            nome = form['nome'].value()
            descricao = form['descricao'].value()
            preco = form['preco'].value()

            if len(nome) > Produto.max_length_nome:
                messages.error(
                    request,
                    f"Campo [Nome] deve conter no máximo {Produto.max_length_nome} caracteres"
                )
            elif len(descricao) > Produto.max_length_descricao:
                messages.error(
                    request,
                    f"Campo [Descrição] deve conter no máximo {Produto.max_length_descricao} caracteres"
                )
            elif float(preco) < 0:
                messages.error(
                    request,
                    f"Campo [Preço] deve conter um valor de no mínimo 0.00"
                )
            else:
                Produto.objects.create(
                    nome = nome,
                    descricao = descricao,
                    preco = preco
                )
                messages.success(
                    request,
                    "Produto cadastrado com sucesso!"
                )
        else:
            messages.error(request, "Dados do formulário inválidos")

    return redirect(home)


def editar(request, id_produto):
    produto = Produto.objects.get(id_produto=id_produto)
    form = ProdutoUpdateForm(instance=produto)

    return render(request, r'catalogo\atualizar.html', {"produto": produto, "form": form})


def update(request, id_produto):
    produto = Produto.objects.get(id_produto=id_produto)
    form = ProdutoUpdateForm(request.POST, instance=produto)
    if request.method == 'POST':
        if form.is_valid():
            nome = form['nome'].value()
            descricao = form['descricao'].value()
            preco = form['preco'].value()

            if len(nome) > Produto.max_length_nome:
                messages.error(
                    request,
                    f"Campo [Nome] deve conter no máximo {Produto.max_length_nome} caracteres"
                )
            elif len(descricao) > Produto.max_length_descricao:
                messages.error(
                    request,
                    f"Campo [Descrição] deve conter no máximo {Produto.max_length_descricao} caracteres"
                )
            elif float(preco) < 0:
                messages.error(
                    request,
                    f"Campo [Preço] deve conter um valor de no mínimo 0.00"
                )
            else:
                produto.nome = nome
                produto.descricao = descricao
                produto.preco = preco
                produto.save()
                messages.success(
                    request,
                    f"Produto código {produto.id_produto} atualizado com sucesso!"
                )
        else:
            messages.error(request, "Dados do formulário inválidos")

    return redirect(home)


def excluir(request, id_produto):
    produto = Produto.objects.get(id_produto=id_produto)
    return render(request, r'catalogo\deletar.html', {'produto': produto})


def delete(request, id_produto):
    produto = Produto.objects.get(id_produto=id_produto)
    if request.method == 'POST':
        produto.delete()
        messages.success(
            request,
            f"Produto código {id_produto} excluído com sucesso!"
        )
    return redirect(home)
