from django.db import models
#from django.contrib.auth.models import User
from accounts.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime


class Tabela(models.Model):
    anoAtual = datetime.datetime.now().year
    nome = models.CharField(max_length=50)
    mes = models.IntegerField(blank=False, null=False, validators=[MaxValueValidator(12), MinValueValidator(1)])
    ano = models.IntegerField(default=anoAtual, blank=False, null=False)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    criada_em = models.DateField(default=timezone.now)
    def __str__(self):
        return self.nome


class Atividade(models.Model):
    descricao = models.CharField(max_length=50)
    duracao = models.IntegerField(blank=True, null=True, validators=[MaxValueValidator(8), MinValueValidator(1)])
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    #item = models.ForeignKey(ItemTabela, on_delete='CASCADE')

    def __str__(self):
        return f"{self.descricao} - {self.duracao}h"


class ItemTabela(models.Model):
    data = models.DateField()
    tabela = models.ForeignKey(Tabela, on_delete=models.CASCADE, related_name='itensTabela')
    atividades = models.ManyToManyField(Atividade, related_name='itens')
    autor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"Item da Table {self.tabela}"




