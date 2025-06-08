from django.db import models
from customers.models import Customer


class VehicleType(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Nome'
    )

    description = models.TextField(
        blank=True,
        null=True,
        verbose_name='Descrição'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,  # Preenche automaticamente com a data e hora de criação
        verbose_name='Criado em'
    )

    updated_at = models.DateTimeField(
        auto_now=True,  # Preenche automaticamente com a data e hora da última atualização
        verbose_name='Atualizado em'
    )

    class Meta:
        verbose_name = 'Tipo de Veiculo'
        verbose_name_plural = 'Tipos de Veiculos'

    def __str__(self):
        return self.name


class Vehicle(models.Model):
    vehicle_type = models.ForeignKey(
        VehicleType,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Tipo de Veiculo'
    )
    license_plate = models.CharField(
        max_length=10,
        unique=True,  # Não pode ter duplicação
        verbose_name='Placa'
    )
    brand = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Marca'
    )
    model = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Modelo'
    )
    color = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name='Cor'
    )
    owner = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='vehicles',
        verbose_name='Proprietário'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,  # Preenche automaticamente com a data e hora de criação
        verbose_name='Criado em'
    )

    updated_at = models.DateTimeField(
        auto_now=True,  # Preenche automaticamente com a data e hora da última atualização
        verbose_name='Atualizado em'
    )

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'

    def __str__(self):
        return self.license_plate
