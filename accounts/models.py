from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nome = models.CharField(default='***', max_length=100)
    sobrenome = models.CharField(default='***', max_length=100)
    matricula = models.CharField(default='***', max_length=9)
    chefia = models.CharField(default='***', max_length=100)
    setor = models.CharField(default='***', max_length=100)
    email = models.EmailField(default='a@b.com', null=False, blank=False)
    usuario = models.CharField(default='***', max_length=100)
    entrada = models.CharField(default='***', max_length=100)
    saidaAlmoco = models.CharField(default='***', max_length=100)
    voltaAlmoco = models.CharField(default='***', max_length=100)
    saida = models.CharField(default='***', max_length=100)

