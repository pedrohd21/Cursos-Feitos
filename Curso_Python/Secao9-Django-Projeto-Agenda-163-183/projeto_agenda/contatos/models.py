from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    

class Contato(models.Model):
    nome = models.CharField(max_length=60)
    sobrenome = models.CharField(max_length=60, blank=True)
    telefone = models.CharField(max_length=60)
    email = models.CharField(max_length=60, blank=True)
    data_criacao = models.DateField(default=timezone.now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome
    

