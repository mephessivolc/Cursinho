from django.db import models

from cursinho.alunos.models import RegisterAluno
from cursinho.accounts.models import User
# Create your models here.

class RegisterPeriodo(models.Model):
    name = models.CharField('Identificação', max_length=10)

    class Meta:
        verbose_name = 'Período'
        verbose_name_plural = 'Períodos'
        ordering = ['name']

class RegisterSala(models.Model):
    name = models.CharField('Nome', max_length=20)
    iden = models.CharField('Identificação', max_length=10)
    qtd = models.IntegerField('Capacidade Máxima')

    class Meta:
        verbose_name = 'Sala'
        verbose_name_plural = 'Salas'
        ordering = ['iden']

class RegisterEscola(models.Model):
    name = models.CharField('Nome', max_length=100)

    class Meta:
        verbose_name = 'Escola'
        verbose_name_plural = 'Escolas'

class RegisterEnd(models.Model):
    end = models.CharField('Endereço', max_length=100, )
    numero = models.CharField('Numero', max_length=10, )
    cep = models.CharField('CEP', max_length=10, blank=True)
    bairro = models.CharField('Bairro', max_length=30, blank=True)
    comp = models.CharField('Complemento', max_length=30, blank=True)
    idPupil = models.OneToOneField(RegisterAluno,
        blank=True, null=True, on_delete=models.CASCADE,
        editable=False,
    )
    idUser = models.OneToOneField(User,
        blank=True, null=True, on_delete=models.CASCADE,
        editable=False,
    )

    def __str__(self):
        return self.end+' '+self.numero+' '+self.bairro+' '+self.comp

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

class RegisterContact(models.Model):
    tel = models.CharField('Telefone', max_length = 15, blank=True, null=True)
    cel = models.CharField('Celular', max_length = 20, blank=True, null=True)
    email = models.EmailField('Email', blank=True, null=True)
    idPupil = models.OneToOneField(RegisterAluno,
        blank=True, null=True, on_delete=models.CASCADE,
        editable=False,
    )

    def __str__(self):
        if self.idPupil is not None:
            return self.idPupil.name

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
