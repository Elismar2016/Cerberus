from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from datetime import datetime
from django.core.exceptions import ValidationError

class CustomUser(AbstractUser):
    USER_TYPES = (
        ("supervisor", "Supervisor"),
        ("motorista", "Motorista"),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES, default="motorista")

    groups = models.ManyToManyField(
        Group,
        related_name="customuser_groups",  # Nome exclusivo para evitar conflito
        blank=True,
        help_text="Os grupos aos quais o usuário pertence.",
        verbose_name="grupos",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="customuser_permissions",  # Nome exclusivo para evitar conflito
        blank=True,
        help_text="Permissões específicas para o usuário.",
        verbose_name="permissões de usuário",
    )

    def __str__(self):
        return self.username

    def is_supervisor(self):
        return self.user_type == "supervisor"

    def is_motorista(self):
        return self.user_type == "motorista"


class Veiculo(models.Model):
    STATUS_CHOICES = [
        ("em manutenção", "Em manutenção"),
        ("em revisão", "Em revisão"),
        ("disponível", "Disponível"),
    ]

    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=50)
    odometro = models.IntegerField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="disponível"
    )

    def __str__(self):
        return f"{self.modelo} - {self.placa}"


class Supervisor(models.Model):

    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={"user_type": "supervisor"},
    )
    matricula = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return self.user.username


class Motorista(models.Model):
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        limit_choices_to={"user_type": "motorista"},
    )
    matricula = models.CharField(max_length=12, unique=True)
    cnh = models.CharField(max_length=12, unique=True)
    categoria = models.CharField(max_length=2)
    validade_cnh = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username
    def is_habilitacao_valida(self):
        return self.validade_cnh >= datetime.now().date()

class Viagem(models.Model):
    class Meta:
        verbose_name = ("Viagem")
        verbose_name_plural = ("Viagens")
        
    STATUS_CHOICES = [
        ("em andamento", "Em andamento"),
        ("finalizada", "Finalizada"),
        ("agendada", "Agendada"),
        ("cancelada", "Cancelada"),
    ]

    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    destino = models.CharField(max_length=255)
    odometro_inicial = models.IntegerField(editable=False)
    data_partida = models.DateTimeField()
    odometro_final = models.IntegerField(null=True, blank=True)
    data_chegada = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="agendada")

    def save(self, *args, **kwargs):
        
        if not self.pk: 
            ultima_viagem = Viagem.objects.filter(veiculo=self.veiculo, status="finalizada").order_by('-data_chegada').first()
            if ultima_viagem:
                self.odometro_inicial = ultima_viagem.odometro_final
            else:
                self.odometro_inicial = self.veiculo.odometro
        
        super().save(*args, **kwargs)

       
        if self.status == "finalizada" and self.odometro_final is not None:
            veiculo = self.veiculo
            veiculo.odometro = self.odometro_final
            veiculo.status = "disponível"
            veiculo.save()

    def clean(self):
        
        if self.veiculo.status != "disponível":
            raise ValidationError("O veículo deve estar com o status 'disponível' para ser incluído em uma viagem.")
        if not self.motorista.ativo:
            raise ValidationError("O motorista deve estar ativo para solicitar uma viagem.")
        if not self.motorista.is_habilitacao_valida():
            raise ValidationError("A habilitação do motorista deve estar válida para solicitar uma viagem.")
        if self.odometro_final is not None and self.odometro_final <= self.odometro_inicial:
            raise ValidationError("O odômetro final deve ser maior que o odômetro inicial.")

    def __str__(self):
        return f"{self.destino} - {self.status}"