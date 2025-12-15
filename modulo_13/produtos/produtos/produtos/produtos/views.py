from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Produto
from .forms import ProdutoForm

def lista_produtos(request):
    busca = request.GET.get('q')
    produtos = Produto.objects.all()

    if busca:
        produtos = produtos.filter(nome__icontains=busca)

    paginator = Paginator(produtos, 5)
    page = request.GET.get('page')
    produtos = paginator.get_page(page)

    return render(request, 'produtos/lista.html', {'produtos': produtos})

def criar_produto(request):
    form = ProdutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'produtos/form.html', {'form': form})

def atualizar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    form = ProdutoForm(request.POST or None, instance=produto)
    if form.is_valid():
        form.save()
        return redirect('lista_produtos')
    return render(request, 'produtos/form.html', {'form': form})

def deletar_produto(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/confirmar_delete.html', {'produto': produto})
