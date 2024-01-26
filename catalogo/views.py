from django.shortcuts import render, redirect
from catalogo.models import *
from catalogo.forms import *

# Create your views here.
def home(request):
    if request.path == '/':
        return redirect('')
    produtos = Produto.objects.all()
    return render(request, "index.html", {"produtos": produtos})


def cadastrar(request):
    return render(request, "cadastrar.html")


def insert(request):
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    preco = request.POST.get('preco')
    Produto.objects.create(nome=nome, descricao=descricao, preco=preco)
    return redirect(home)


def editar(request, id_produto):
    produto = Produto.objects.get(id_produto=id_produto)
    form = ProdutoUpdateForm(instance=produto)

    if request.method == 'POST':
        form = ProdutoUpdateForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            # produto.nome = form['nome'].value()
            # produto.descricao = form['descricao'].value()
            # produto.preco = form['preco'].value()

            # produto.save()
        else:
            form = ProdutoUpdateForm(instance=produto)

    return render(request, 'atualizar.html', {"produto": produto, "form": form})


def update(request, id_produto):
    nome = request.POST.get('nome')
    descricao = request.POST.get('descricao')
    preco = request.POST.get('preco')
    produto = Produto.objects.get(id_produto=id_produto)
    produto.nome = nome
    produto.descricao = descricao
    produto.preco = preco
    produto.save()
    return redirect(home)


def deletar(request, id_produto):
    produto = Produto.objects.get(id_produto=id_produto)
    # form = ProdutoDeleteForm(request.POST)
    # if form.is_valid() and form.cleaned_data['confirmar']:
    produto.delete()
    produtos = Produto.objects.all()
    return render(request, "index.html", {"produtos": produtos})
