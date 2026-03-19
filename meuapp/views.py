from django.shortcuts import render, redirect
from .forms import PessoaForm
from .models import Pessoa


def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'meuapp/list.html', {'pessoas': pessoas})

def criar_pessoa(request):
    
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
    return render(request, 'meuapp/form.html', {'form': form})

def atualizar_pessoa(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'meuapp/form.html', {'form': form})

def deletar_pessoa(request, pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('listar_pessoas')
    return render(request, 'meuapp/confirmar_delete.html', {'pessoa': pessoa})
