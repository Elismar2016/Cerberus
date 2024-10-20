from django.db import models

# Create your models here.

from django.contrib.auth.models import User

class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)
    ano = models.IntegerField()

class Motorista(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cnh = models.CharField(max_length=12)
    categoria = models.CharField(max_length=2)

class Viagem(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(null=True, blank=True)
    localizacao_inicio = models.CharField(max_length=100)
    localizacao_fim = models.CharField(max_length=100, null=True, blank=True)
