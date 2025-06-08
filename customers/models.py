from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    # Relacionamento com o modelo User do Django (um-para-um)
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='customers',
        verbose_name='Usuário'
    )

    name = models.CharField(
        max_length=100,
        verbose_name='Nome'
    )
    
    cpf = models.CharField(
        max_length=15,
        blank=True,  # Permite que o campo seja deixado em branco
        null=True,
        verbose_name='CPF'
    )

    phone = models.CharField(
        max_length=15,
        blank=True,
        null=True,  # Permite que o campo seja nulo no banco de dados
        verbose_name='Telefone'
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
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
    
    def __str__(self):
        return self.name
