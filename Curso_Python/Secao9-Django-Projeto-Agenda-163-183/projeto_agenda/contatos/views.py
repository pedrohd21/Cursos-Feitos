from django.shortcuts import render
from .models import Contato     # Importar as classes que ta no modelss


def index(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/index.html', {
        'contatos': contatos
    }) ###  Vai adicionar a classe contatos


def ver_contato(request, contato_id):
    contato = Contato.objects.get(id=contato_id)
    return render(request, 'contatos/ver_contato.html', {
        'contato': contato
    }) ###  Vai adicionar a classe contatos